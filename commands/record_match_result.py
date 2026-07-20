from commands.context import Context

from .base import BaseCommand


class RecordMatchResultCmd(BaseCommand):
    """Command used to record the result of a match."""

    def __init__(self, tournament, match, winner):
        # Store the tournament, match, and winner
        self.tournament = tournament
        self.match = match
        self.winner = winner

    def execute(self):
        # Record the match result
        self.tournament.record_match_result(
            self.match,
            self.winner,
        )

        # Return to the tournament view
        return Context(
            "tournament-view",
            tournament=self.tournament,
        )
