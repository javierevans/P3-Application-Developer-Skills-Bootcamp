from commands import ClubListCmd, NoopCmd
from models import ClubManager

from ..base_screen import BaseScreen


class TournamentSelectClub(BaseScreen):
    """Screen for selecting a club."""

    def __init__(self, tournament):
        self.tournament = tournament
        self.club_manager = ClubManager()

    def display(self):

        print("=" * 50)
        print("Select a Club")
        print("=" * 50)

        for i, club in enumerate(self.club_manager.clubs, start=1):
            print(f"{i}. {club.name}")

        print()
        print("Type X to return.")

    def get_command(self):

        while True:

            choice = self.input_string()

            if choice.upper() == "X":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament,
                )

            if choice.isdigit():

                choice = int(choice)

                if choice in range(1, len(self.club_manager.clubs) + 1):

                    return NoopCmd(
                        "tournament-register-player",
                        tournament=self.tournament,
                        club=self.club_manager.clubs[choice - 1],
                    )

            print("Invalid selection.")