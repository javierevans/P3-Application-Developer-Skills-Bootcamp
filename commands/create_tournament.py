from commands.context import Context
from models import ClubManager
from models.tournament import Tournament


from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command used to create a tournament."""

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_rounds,
        description,
    ):
        # Store the tournament information
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description

    def execute(self):
        # Create the tournament
        tournament = Tournament(
            self.name,
            self.location,
            self.start_date,
            self.end_date,
            int(self.number_of_rounds),
            self.description,
        )

        # Save the tournament
        tournament.save(
            f"data/{self.name.replace(' ', '_')}.json"
        )

        # Reload the club list
        cm = ClubManager()

        # Return to the main menu
        return Context(
            "main-menu",
            clubs=cm.clubs,
        )
