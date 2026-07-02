from .rounds import Round
from .player import Player
from .match import Match
import json
from pathlib import Path

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
        if player is not None and player not in self.players:
            self.players.append(player)
            self.player_scores[player.chess_id] = 0
            
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
        
        round_one = Round(1) 
        
        self.generate_matches(round_one)
        
        self.add_round(round_one)
        
        self.current_round = 1
        
        self.save(round_one)
        
        return round_one
    
    def can_start(self):
        if len(self.players) < 8:
            return False
        if len(self.rounds) > 0:
                return False
        
        return True
    
    def generate_matches(self, round_obj):
        players = self.players
        
        players = sorted(players, key =lambda player: player.chess_id)
        
        half = len(players)//2
        top_half = players[:half]
        bottom_half = players[half:]
        
        for i in range(len(top_half)):
            
            player_one = top_half[i]
            player_two = bottom_half[i]
            
            match = Match([player_one, player_two])
            
            round_obj.add_match(match)
    
    
    def record_match_result(self, match, winner = None):
        match.mark_completed(winner)
        
        #get the two players 
        player_one, player_two = match.players
        
        if winner == player_one:
            self.player_scores[player_one.chess_id] += 1
        elif winner == player_two:
            self.player_scores[player_two.chess_id] += 1
        else:
            self.player_scores[player_one.chess_id] += 0.5
            self.player_scores[player_two.chess_id] += 0.5
        
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
        
        return cls(
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
    
    @classmethod
    def load(cls, filepath):
        with open(filepath, "r") as file:
         data = json.load(file)

        return cls.from_dict(data)