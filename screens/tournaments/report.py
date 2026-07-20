from commands import NoopCmd

from ..base_screen import BaseScreen


class TournamentReport(BaseScreen):
    """Screen for viewing tournament information."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("=" * 50)
        print("Tournament Report")
        print("=" * 50)
        print()

        print(f"Name: {self.tournament.name}")
        print(f"Location: {self.tournament.location}")
        print(f"Start Date: {self.tournament.start_date}")
        print(f"End Date: {self.tournament.end_date}")
        print(f"Rounds: {self.tournament.current_round}/{self.tournament.number_of_rounds}")
        print(f"Players: {len(self.tournament.players)}")
        print()

        print("Players")
        print("-" * 50)

        for player in self.tournament.players:
            score = self.tournament.player_scores[player.chess_id]
            print(f"{player.name:<20} {score}")

    def get_command(self):
        self.input_string("Press Enter to return")

        return NoopCmd(
            "tournament-view",
            tournament=self.tournament,
        )
