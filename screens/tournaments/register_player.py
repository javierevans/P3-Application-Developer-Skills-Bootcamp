from commands import NoopCmd

from ..base_screen import BaseScreen


class TournamentRegisterPlayer(BaseScreen):
    """Screen for adding players to a tournament."""

    def __init__(self, tournament, club):
        # Store the tournament and selected club
        self.tournament = tournament
        self.club = club

    def display(self):
        print("=" * 50)
        print(self.club.name)
        print("=" * 50)
        print()

        # Show every player in the club
        for index, player in enumerate(self.club.players, start=1):
            if player in self.tournament.players:
                status = "(Added)"
            else:
                status = ""

            print(f"{index}. {player.name} {status}")

        print()
        print(f"Players in Tournament: {len(self.tournament.players)}/8")
        print()
        print("Choose a player to add.")
        print("Type X to return.")

    def get_command(self):
        while True:
            choice = self.input_string()

            # Return to the tournament screen
            if choice.upper() == "X":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament,
                )

            if choice.isdigit():
                choice = int(choice)

                if choice in range(1, len(self.club.players) + 1):
                    player = self.club.players[choice - 1]

                    # Don't allow more than 8 players
                    if len(self.tournament.players) >= 8:
                        return NoopCmd(
                            "tournament-view",
                            tournament=self.tournament,
                        )

                    # Don't add the same player twice
                    if player not in self.tournament.players:
                        self.tournament.add_player(player)

                    # Continue adding players
                    return NoopCmd(
                        "tournament-register-player",
                        tournament=self.tournament,
                        club=self.club,
                    )

            print("Invalid selection.")
