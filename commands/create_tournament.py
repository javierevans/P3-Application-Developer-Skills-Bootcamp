from commands.context import Context
from models.tournament import Tournament
from models import ClubManager

from .base import BaseCommand

class TournamentCreateCmd(BaseCommand):
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_rounds,
        description,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        
    def execute(self):
        tournament = Tournament(
            self.name,
            self.location,
            self.start_date,
            self.end_date,
            int(self.number_of_rounds),
            self.description,
    )

        tournament.save(
            f"data/{self.name.replace(' ', '_')}.json"
    )

        cm = ClubManager()

        return Context(
            "main-menu",
            clubs=cm.clubs,
)
    