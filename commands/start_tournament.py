from commands.context import Context

from .base import BaseCommand


class StartTournamentCmd(BaseCommand):
    """Command used to start a tournament."""

    def __init__(self, tournament):
        # Store the tournament
        self.tournament = tournament

    def execute(self):
        # Start the tournament
        self.tournament.start_tournament()

        # Return to the tournament view
        return Context(
            "tournament-view",
            tournament=self.tournament,
        )
