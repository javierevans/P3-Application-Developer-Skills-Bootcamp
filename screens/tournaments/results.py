from commands import NoopCmd

from ..base_screen import BaseScreen


class TournamentResults(BaseScreen):
    """Screen for viewing the current round."""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):

        print("=" * 50)
        print("Current Round")
        print("=" * 50)
        print()

        # Make sure the tournament has started
        if not self.tournament.rounds:
            print("Tournament has not started yet.")
            return

        # Get the current round
        current_round = self.tournament.rounds[-1]

        print(f"Round {current_round.round_number}")
        print()

        # Display every match
        for i, match in enumerate(current_round.matches, start=1):

            player_one, player_two = match.players

            if match.completed:

                if match.winner is None:
                    result = "Tie"

                else:
                    result = f"Winner: {match.winner.name}"

            else:
                result = "Not Played"

            print(f"{i}. {player_one.name} vs {player_two.name} ({result})")

        print()
        print("Choose a match.")
        print("Type X to return.")

    def get_command(self):

        # Tournament hasn't started yet
        if not self.tournament.rounds:

            self.input_string("Press Enter")

            return NoopCmd(
                "tournament-view",
                tournament=self.tournament,
            )

        current_round = self.tournament.rounds[-1]

        while True:

            choice = self.input_string()

            if choice.upper() == "X":

                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament,
                )

            if choice.isdigit():

                choice = int(choice)

                if choice in range(1, len(current_round.matches) + 1):

                    return NoopCmd(
                        "match-result",
                        tournament=self.tournament,
                        match=current_round.matches[choice - 1],
                    )

            print("Invalid selection.")
