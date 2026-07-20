from commands.context import Context
from models import TournamentManager

from .base import BaseCommand


class TournamentListCmd(BaseCommand):
    """Command used to load the list of tournaments."""

    def execute(self):
        # Load every saved tournament
        tm = TournamentManager()

        # Display the tournament list screen
        return Context(
            "tournament-list",
            tournaments=tm.tournaments,
        )
