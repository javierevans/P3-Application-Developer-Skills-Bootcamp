import json
from pathlib import Path

class TournamentManager:
    def __init__(self):
        self.data_folder = Path("data")
        self.tournaments = []
        
        
     
    def create( self, name, location, start_date, end_date, number_of_rounds, description): 
        filepath = Path("data") / (name.replace(" ", "_") + ".json")

        tournament = Tournament( name, location, start_date, end_date, number_of_rounds, description,)

        tournament.save(filepath)

        self.tournaments.append(tournament)

        return tournament
