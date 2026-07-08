from models.tournament import Tournament
from models.player import Player
import random

# -----------------------------
# Create Tournament
# -----------------------------
tournament = Tournament(
    name="Full Tournament Test",
    location="Test City",
    start_date="01-07-2026",
    end_date="02-07-2026",
    number_of_rounds=4,
    description="Automatic Tournament Test"
)

# -----------------------------
# Create Players
# -----------------------------
players = [
    Player("John", "john@test.com", "1001", "01-01-1995"),
    Player("Sarah", "sarah@test.com", "1002", "02-02-1996"),
    Player("Ryan", "ryan@test.com", "1003", "03-03-1997"),
    Player("Mike", "mike@test.com", "1004", "04-04-1998"),
    Player("Emma", "emma@test.com", "1005", "05-05-1999"),
    Player("Kate", "kate@test.com", "1006", "06-06-2000"),
    Player("Chris", "chris@test.com", "1007", "07-07-2001"),
    Player("Alex", "alex@test.com", "1008", "08-08-2002"),
]

for player in players:
    tournament.add_player(player)

print("=" * 60)
print("STARTING TOURNAMENT")
print("=" * 60)

tournament.start_tournament()

# -----------------------------
# Play Every Round
# -----------------------------
while tournament.current_round <= tournament.number_of_rounds:

    current_round = tournament.rounds[-1]

    print(f"\nROUND {current_round.round_number}")
    print("-" * 60)

    for match in current_round.matches:

        player_one, player_two = match.players

        print(f"{player_one.name} vs {player_two.name}")

        # Randomly choose:
        # player one wins
        # player two wins
        # tie

        result = random.randint(0, 2)

        if result == 0:
            winner = player_one
            print(f"Winner: {player_one.name}")

        elif result == 1:
            winner = player_two
            print(f"Winner: {player_two.name}")

        else:
            winner = None
            print("Tie")

        tournament.record_match_result(match, winner)

    # Tournament finished
    if tournament.current_round == tournament.number_of_rounds:
        last_round = tournament.rounds[-1]

        if last_round.is_completed():
            break

print("\n" + "=" * 60)
print("FINAL SCORES")
print("=" * 60)

players = sorted(
    tournament.players,
    key=lambda p: tournament.player_scores[p.chess_id],
    reverse=True,
)

for player in players:
    print(
        f"{player.name:<15}"
        f"{tournament.player_scores[player.chess_id]}"
    )

print("\nTournament Complete!")