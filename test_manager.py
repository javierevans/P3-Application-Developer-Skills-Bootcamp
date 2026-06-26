from models.tournament_manager import TournamentManager

tm = TournamentManager()

print("Tournaments loaded:")
print(len(tm.tournaments))

for tournament in tm.tournaments:
    print(tournament)
    