from models.tournament import Tournament
from models.player import Player

# Create tournament
tournament = Tournament(
    name="Test Tournament",
    location="Test City",
    start_date="01-07-2026",
    end_date="02-07-2026",
    number_of_rounds=4,
    description="Testing Tournament"
)

# Create 8 test players
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

# Add players
for player in players:
    tournament.add_player(player)

print("=" * 50)
print("Tournament Created")
print("=" * 50)

print(f"Players Added: {len(tournament.players)}")

# Start tournament
round_one = tournament.start_tournament()

if round_one is None:
    print("Tournament failed to start.")
    quit()

print("\nRound 1 Matches")
print("-" * 50)

for match in round_one.matches:
    p1, p2 = match.players
    print(f"{p1.name} vs {p2.name}")

print("\nRecording Results...")
print("-" * 50)

# First player wins every match
for match in round_one.matches:
    tournament.record_match_result(match, match.players[0])

print("\nScores")
print("-" * 50)

for player in tournament.players:
    print(f"{player.name}: {tournament.player_scores[player.chess_id]}")

print(f"\nCurrent Round: {tournament.current_round}")

if len(tournament.rounds) > 1:
    round_two = tournament.rounds[1]

    print("\nRound 2 Matches")
    print("-" * 50)

    for match in round_two.matches:
        p1, p2 = match.players
        print(f"{p1.name} vs {p2.name}")
else:
    print("\nRound 2 was not created.")