from models.tournament import Tournament
from models.player import Player
import random

# -----------------------------
# Create Tournament
# -----------------------------
tournament = Tournament(
    name="No Repeat Opponent Test",
    location="Test City",
    start_date="01-07-2026",
    end_date="02-07-2026",
    number_of_rounds=4,
    description="Testing Repeat Opponents"
)

# -----------------------------
# Players
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

tournament.start_tournament()

# -----------------------------
# Play Entire Tournament
# -----------------------------
while tournament.current_round <= tournament.number_of_rounds:

    current_round = tournament.rounds[-1]

    for match in current_round.matches:

        winner = random.choice([
            match.players[0],
            match.players[1],
            None
        ])

        tournament.record_match_result(match, winner)

    if (
        tournament.current_round == tournament.number_of_rounds
        and tournament.rounds[-1].is_completed()
    ):
        break

# -----------------------------
# Check For Repeat Opponents
# -----------------------------
played_matches = set()
duplicate_found = False

for round_obj in tournament.rounds:

    for match in round_obj.matches:

        p1 = match.players[0].chess_id
        p2 = match.players[1].chess_id

        pairing = tuple(sorted([p1, p2]))

        if pairing in played_matches:
            print("\n❌ DUPLICATE FOUND")
            print(
                f"{match.players[0].name} "
                f"played "
                f"{match.players[1].name} "
                f"more than once."
            )
            duplicate_found = True

        else:
            played_matches.add(pairing)

if not duplicate_found:
    print("\n✅ SUCCESS")
    print("No repeated opponents were found.")