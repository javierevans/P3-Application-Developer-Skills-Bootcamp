from commands import ClubListCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentList(BaseScreen):

    def __init__(self, tournaments):
        self.tournaments = tournaments

    def display(self):
        for idx, tournament in enumerate(self.tournaments, 1):
            print(idx, tournament.name)

    def get_command(self):
        while True:
            print("Enter a tournament number to view it.")
            print("Type X to return.")

            value = self.input_string()

            if value.isdigit():
                value = int(value)

                if value in range(1, len(self.tournaments) + 1):
                    return NoopCmd(
                        "tournament-view",
                        tournament=self.tournaments[value - 1]
                    )

            elif value.upper() == "X":
                return ClubListCmd()
