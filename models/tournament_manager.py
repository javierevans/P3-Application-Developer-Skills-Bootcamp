import json
from pathlib import Path

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []

        for filepath in datadir.iterdir():
        
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    tournament = Tournament.load(filepath)
                    self.tournaments.append(tournament)
                except json.JSONDecodeError:
                    print(filepath, "is an invalid JSON file.")

    def create(self, name, location, start_date, end_date, number_of_rounds, description, ):
        filepath = self.data_folder / (name.replace(" ", "_") + ".json")

        tournament = Tournament(name, location, start_date, end_date, number_of_rounds, description,)

        tournament.save(filepath)

        self.tournaments.append(tournament)

        return tournament