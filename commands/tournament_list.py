from commands.context import Context
from models import TournamentManager

from .base import BaseCommand


class TournamentListCmd(BaseCommand):
    """Command to get the list of tournaments"""

    def execute(self):
        tm = TournamentManager()
        return Context("tournament-list", tournaments = tm.tournaments)
