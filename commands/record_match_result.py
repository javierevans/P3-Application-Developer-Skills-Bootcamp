from commands.context import Context

from .base import BaseCommand


class RecordMatchResultCmd(BaseCommand):
    """Records the result of a match."""

    def __init__(self, tournament, match, winner):
        self.tournament = tournament
        self.match = match
        self.winner = winner

    def execute(self):
        self.tournament.record_match_result(
            self.match,
            self.winner
        )

        return Context(
            "tournament-view",
            tournament=self.tournament,
        )