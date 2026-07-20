from commands import NoopCmd

from ..base_screen import BaseScreen


class TournamentStandings(BaseScreen):
    """Screen for displaying the current standings."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("=" * 50)
        print("Tournament Standings")
        print("=" * 50)
        print()

        # Sort players by score
        players = sorted(
            self.tournament.players,
            key=lambda player: (
                self.tournament.player_scores[player.chess_id],
                player.chess_id,
            ),
            reverse=True,
        )

        # Display each player's score
        for i, player in enumerate(players, start=1):
            score = self.tournament.player_scores[player.chess_id]

            print(f"{i}. {player.name:<20} {score}")

        print()

    def get_command(self):
        self.input_string("Press Enter to return")

        return NoopCmd(
            "tournament-view",
            tournament=self.tournament,
        )
