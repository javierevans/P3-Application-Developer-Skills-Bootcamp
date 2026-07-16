from commands import ClubListCmd, NoopCmd, StartTournamentCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed when viewing a Tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("=" * 50)
        print(self.tournament.name)
        print("=" * 50)
        print(f"Location: {self.tournament.location}")
        print(
            f"Current Round: {self.tournament.current_round}/{self.tournament.number_of_rounds}"
        )
        player_count = len(self.tournament.players)

        if player_count % 2 == 0 and player_count >= 8:
            status = "Ready to Start"
        else:
            status = "Need at least 8 players and an even number"

        print(f"Players: {player_count}")
        print(status)
        print()

        print("1. Register Players")
        print("2. Start Tournament")
        print("3. Enter Match Results")
        print("4. View Standings")
        print("5. Reports")
        print("0. Back")
        print("=" * 50)

    def get_command(self):
        while True:
         choice = self.input_string("Choose an option")

        # Register players
         if choice == "1":
            return NoopCmd(
                "tournament-select-club",
                tournament=self.tournament,
            )

        # Start the tournament
         elif choice == "2":
            return StartTournamentCmd(
                self.tournament,
            )

        # Enter match results
         elif choice == "3":
            return NoopCmd(
                "tournament-results",
                tournament=self.tournament,
            )

        # View standings
         elif choice == "4":
            return NoopCmd(
                "tournament-standings",
                tournament=self.tournament,
            )

        # Tournament report
         elif choice == "5":
            return NoopCmd(
                "tournament-report",
                tournament=self.tournament,
            )

        # Return to tournament list
         elif choice == "0":
            return ClubListCmd()

         print("Invalid option.")