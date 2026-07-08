from models.tournament import Tournament
from models.player import Player

# -----------------------------
# Create Tournament
# -----------------------------
tournament = Tournament(
    name="Floating Test",
    location="Test City",
    start_date="01-07-2026",
    end_date="02-07-2026",
    number_of_rounds=4,
    description="Floating Player Test"
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
# Round 1
# -----------------------------
round_one = tournament.start_tournament()

print("=" * 60)
print("ROUND 1")
print("=" * 60)

for match in round_one.matches:
    p1, p2 = match.players
    print(f"{p1.name} vs {p2.name}")

# -----------------------------
# Force an odd score group
# -----------------------------
#
# Winners:
# John
# Sarah
# Ryan
#
# Tie:
# Mike vs Alex
#
# Scores:
#
# 1.0 -> John, Sarah, Ryan
# 0.5 -> Mike, Alex
# 0.0 -> Emma, Kate, Chris
#
# This creates TWO odd score groups.
#

tournament.record_match_result(round_one.matches[0], round_one.matches[0].players[0])  # John wins
tournament.record_match_result(round_one.matches[1], round_one.matches[1].players[0])  # Sarah wins
tournament.record_match_result(round_one.matches[2], round_one.matches[2].players[0])  # Ryan wins
tournament.record_match_result(round_one.matches[3], None)                             # Tie

# -----------------------------
# Round 2
# -----------------------------
round_two = tournament.rounds[-1]

print("\n" + "=" * 60)
print("ROUND 2")
print("=" * 60)

for match in round_two.matches:
    p1, p2 = match.players
    print(f"{p1.name} vs {p2.name}")

print("\nCurrent Scores")
print("-" * 60)

for player in sorted(
    tournament.players,
    key=lambda p: tournament.player_scores[p.chess_id],
    reverse=True
):
    print(f"{player.name:<10} {tournament.player_scores[player.chess_id]}")