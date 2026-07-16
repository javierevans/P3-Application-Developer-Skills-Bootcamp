from commands import NoopCmd, RecordMatchResultCmd

from ..base_screen import BaseScreen


class MatchResult(BaseScreen):
    """Screen for entering the result of a match."""

    def __init__(self, tournament, match):
        self.tournament = tournament
        self.match = match

    def display(self):
        player_one, player_two = self.match.players

        print("=" * 50)
        print(f"{player_one.name} vs {player_two.name}")
        print("=" * 50)
        print()

        print("1. " + player_one.name + " Wins")
        print("2. " + player_two.name + " Wins")
        print("3. Tie")
        print("0. Cancel")
        print()

    def get_command(self):

        player_one, player_two = self.match.players

        while True:

            choice = self.input_string("Choose an option")

            if choice == "1":
                return RecordMatchResultCmd(
                    self.tournament,
                    self.match,
                    player_one,
                )

            elif choice == "2":
                return RecordMatchResultCmd(
                    self.tournament,
                    self.match,
                    player_two,
                )

            elif choice == "3":
                return RecordMatchResultCmd(
                    self.tournament,
                    self.match,
                    None,
                )

            elif choice == "0":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament,
                )

            print("Invalid option.")