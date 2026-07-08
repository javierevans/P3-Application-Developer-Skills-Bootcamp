from models.tournament import Tournament
from models.player import Player
import random
import os

# -----------------------------
# Create Tournament
# -----------------------------
tournament = Tournament(
    name="Save Load Test",
    location="Test City",
    start_date="01-07-2026",
    end_date="02-07-2026",
    number_of_rounds=4,
    description="Testing Save and Load"
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

# -----------------------------
# Play One Round
# -----------------------------
tournament.start_tournament()

current_round = tournament.rounds[-1]

for match in current_round.matches:

    winner = random.choice([
        match.players[0],
        match.players[1],
        None
    ])

    tournament.record_match_result(match, winner)

# -----------------------------
# Save Tournament
# -----------------------------
filename = "save_test.json"

tournament.save(filename)

print("=" * 50)
print("TOURNAMENT SAVED")
print("=" * 50)

# -----------------------------
# Load Tournament
# -----------------------------
loaded = Tournament.load(filename)

print("\nTOURNAMENT LOADED\n")

print(f"Name: {loaded.name}")
print(f"Location: {loaded.location}")
print(f"Current Round: {loaded.current_round}")
print(f"Players: {len(loaded.players)}")
print(f"Rounds: {len(loaded.rounds)}")

print("\nScores")

for player in loaded.players:
    score = loaded.player_scores.get(player.chess_id, "Missing")
    print(f"{player.name:<10} {score}")

# -----------------------------
# Cleanup
# -----------------------------
if os.path.exists(filename):
    os.remove(filename)