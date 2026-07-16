

from .rounds import Round
from .player import Player
from .match import Match
import json
import random

from models import player

class Tournament:
    def __init__(self, name, location, start_date, end_date, number_of_rounds, description, current_round = 0 , players = None, rounds = None ):
        self.name = name
        self.location = location 
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.current_round = current_round
        self.players = players if players is not None else []
        self.player_scores = {}
        self.rounds = rounds if rounds is not None else []
        
    def __str__(self): 
        return f"Tournament: {self.name} | Location: {self.location} | Player {len (self.players)}, Round: {self.current_round} / {self.number_of_rounds}"  
    
    def add_player(self, player):
        """Add a player to the tournament."""

    # Don't add duplicate players
        if player is None or player in self.players:
            return False

        self.players.append(player)
        self.player_scores[player.chess_id] = 0

        return True
            
    def add_round(self, round_obj):
        if round_obj is not None and round_obj not in self.rounds:
            self.rounds.append(round_obj)
            
    def serialize(self):
        return{
            "name" : self.name,
            "location" : self.location,
            "start_date" : self.start_date,
            "end_date" : self.end_date ,
            "description" : self.description,
            "current_round" : self.current_round,
            "number_of_rounds" : self.number_of_rounds,
            "players" : [ player.serialize() for player in self.players],
            "rounds" : [round_obj.serialize() for round_obj in self.rounds],  
        }
        
    def save(self, filepath):
        with open(filepath, "w") as file:
            json.dump(self.serialize(), file, indent=4)
            
    def start_tournament(self):
        if not self.can_start():
            return
        
        self.current_round = 1
        
        round_one = Round(1) 
        
        self.generate_matches(round_one)
        
        self.add_round(round_one)
        
        self.save("tournament_round_1.json")
        
        return round_one
    
    def can_start(self):
    # Tournament needs at least 8 players
        if len(self.players) < 8:
            return False

    # Tournament needs an even number of players
        if len(self.players) % 2 != 0:
            return False

    # Tournament has already started
        if len(self.rounds) > 0:
            return False

        return True
    
    def generate_matches(self, round_obj):
        if self.current_round == 1:
            self.generate_first_round_matches(round_obj)
        else:
            self.generate_next_round_matches(round_obj)
        
    def generate_first_round_matches(self, round_obj):
        players = self.players.copy()
            
        random.shuffle(players)
        
        print("\nAfter Shuffle:")
        for player in players:
            print(player.name)
            
        half = len(players)//2
        top_half = players[:half] 
        bottom_half = players[half:]
            
        for i in range(len(top_half)):
                
            player_one = top_half[i]
            player_two = bottom_half[i]
                
            match = Match([player_one, player_two])
                
            round_obj.add_match(match)
    
    def generate_next_round_matches(self, round_obj):
        players = self.sort_players_by_score()
        
        score_groups = self.build_score_groups(players)
        
        self.pair_score_groups(score_groups, round_obj)
                            
    def sort_players_by_score(self):
        return sorted(self.players, key = lambda player: (self.player_scores[player.chess_id], player.chess_id), reverse = True)
            
    def build_score_groups(self,players):
        score_groups = {}
        
        for player in players:
            score = self.player_scores[player.chess_id]
            if score not in score_groups:
                score_groups[score] = []
            score_groups[score].append(player)
        
        return score_groups  
    
    def pair_score_groups(self, score_groups, round_obj):
        
        for score in score_groups:
            group = score_groups[score]
            remaining_players = group.copy()
            
            while remaining_players:
                found_opponent = False
                player_one = remaining_players[0]
                
                for i in range(1, len(remaining_players)):
                    player_two = remaining_players[i]
                    
                    if not self.have_played_before(player_one, player_two):
                        match = Match([player_one, player_two])
                        round_obj.add_match(match)
                        
                        remaining_players.remove(player_one)
                        remaining_players.remove(player_two)
                        found_opponent = True
                        break
                
                if not found_opponent:
                    next_score = score - 0.5
                    
                    if next_score in score_groups:
                       score_groups[next_score].append(player_one)
                       
                    remaining_players.remove(player_one)      
                                       
        
    def have_played_before(self, player_one, player_two):
        for round_obj in self.rounds:
            for match in round_obj.matches:
                if player_one in match.players and player_two in match.players:
                    return True
        return False
    
    
    def record_match_result(self, match, winner = None):
        match.mark_completed(winner)
        
        #get the two players 
        player_one, player_two = match.players
        
        if winner is None:
            self.player_scores[player_one.chess_id] += 0.5
            self.player_scores[player_two.chess_id] += 0.5
        elif winner == player_one:
            self.player_scores[player_one.chess_id] += 1
        elif winner == player_two:
            self.player_scores[player_two.chess_id] += 1
        
        #store round in variable
        current_round = self.rounds[-1]
        
        self.save(f"tournament_round_{self.current_round}.json")
        
        #check if the round is completed
        round_completed = current_round.is_completed()
        if round_completed:
            if self.current_round < self.number_of_rounds:
                self.current_round += 1
                new_round = Round(self.current_round)
                self.generate_matches(new_round)
                self.add_round(new_round)
                self.save(f"tournament_round_{self.current_round}.json")
            else:
                print("Tournament completed!")
                self.save(f"tournament_{self.name}.json")
                
    def rebuild_player_scores(self):
        self.player_scores = {player.chess_id: 0 for player in self.players}
        
        for round_obj in self.rounds:
            for match in round_obj.matches:
                if match.completed:
                    player_one, player_two = match.players
                    winner = match.winner
                    
                    if winner is None:
                        self.player_scores[player_one.chess_id] += 0.5
                        self.player_scores[player_two.chess_id] += 0.5
                    elif winner == player_one:
                        self.player_scores[player_one.chess_id] += 1
                    elif winner == player_two:
                        self.player_scores[player_two.chess_id] += 1

    @classmethod
    def from_dict(cls, data):
        players = [
            Player.from_dict(player_data)
            for player_data in data["players"]
        ]

        rounds = [
            Round.from_dict(round_obj_data)
            for round_obj_data in data["rounds"]
        ]

        tournament = cls(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["number_of_rounds"],
            data["description"],
            data["current_round"],
            players,
            rounds
        )

        tournament.rebuild_player_scores()

        return tournament
    
    @classmethod
    def load(cls, filepath):
        with open(filepath, "r") as file:
         data = json.load(file)

        return cls.from_dict(data)