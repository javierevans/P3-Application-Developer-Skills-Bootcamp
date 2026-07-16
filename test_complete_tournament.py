import random

from models import ClubManager
from models.tournament import Tournament


def print_standings(tournament):
    """Display the current standings."""

    print("\nCurrent Standings")
    print("-" * 40)

    standings = sorted(
        tournament.players,
        key=lambda player: (
            tournament.player_scores[player.chess_id],
            player.chess_id,
        ),
        reverse=True,
    )

    for player in standings:
        score = tournament.player_scores[player.chess_id]
        print(f"{player.name:<25} {score}")

    print()


def main():

    print("=" * 60)
    print("TOURNAMENT TEST")
    print("=" * 60)

    club_manager = ClubManager()

    club = club_manager.clubs[0]

    tournament = Tournament(
        "Tournament Test",
        "New Jersey",
        "07-16-2026",
        "07-17-2026",
        4,
        "Automated Test",
    )

    print("\nAdding Players...\n")

    # Add the first 8 players
    for player in club.players[:10]:
        tournament.add_player(player)
        print(player.name)

    print(f"\nPlayers Added: {len(tournament.players)}")

    print("\nStarting Tournament...\n")

    tournament.start_tournament()

    while tournament.current_round <= tournament.number_of_rounds:

        current_round = tournament.rounds[-1]

        print("=" * 60)
        print(f"ROUND {current_round.round_number}")
        print("=" * 60)

        for match in current_round.matches:

            player_one, player_two = match.players

            print(f"\n{player_one.name} vs {player_two.name}")

            winner = random.choice(
                [
                    player_one,
                    player_two,
                    None,
                ]
            )

            if winner is None:
                print("Result: Tie")

            else:
                print(f"Winner: {winner.name}")

            tournament.record_match_result(match, winner)

        print_standings(tournament)

        if tournament.current_round == tournament.number_of_rounds:

            last_round = tournament.rounds[-1]

            if last_round.is_completed():
                break

    print("=" * 60)
    print("FINAL STANDINGS")
    print("=" * 60)

    print_standings(tournament)

    print("Tournament completed successfully!")


if __name__ == "__main__":
    main()