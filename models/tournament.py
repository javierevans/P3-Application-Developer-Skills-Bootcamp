from .rounds import Round
from .player import Player
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
        self.rounds = rounds if rounds is not None else []
        
    def __str__(self): 
        return f"Tournament: {self.name} | Location: {self.location} | Player {len (self.players)}, Round: {self.current_round} / {self.number_of_rounds}"  
    
    def add_player(self, player):
        if player is not None and player not in self.players:
            self.players.append(player)
            
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