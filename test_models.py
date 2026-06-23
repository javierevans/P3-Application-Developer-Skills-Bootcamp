from models.player import Player
from models.match import Match
from models.rounds import Round
from models.tournament import Tournament


player = Player(
    "Javier",
    "test@test.com",
    "1234",
    "23-06-2004"
)

match = Match([player, player])

round1 = Round(1, [match])

tournament = Tournament(
    "Test Tournament",
    "NJ",
    "2026-01-01",
    "2026-01-02",
    4,
    "Test Tournament",
    1,
    [player],
    [round1]
)

data = tournament.serialize()

print("Serialized:")
print(data)

loaded_tournament = Tournament.from_dict(data)

print("\nLoaded:")
print(loaded_tournament)