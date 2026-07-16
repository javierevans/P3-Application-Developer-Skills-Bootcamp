from commands import ClubListCmd
from screens import (ClubCreate, ClubView, MainMenu, PlayerEdit, PlayerView, 
TournamentCreate, TournamentList,TournamentView,TournamentStandings,TournamentReport, TournamentResults,
 TournamentSelectClub, TournamentRegisterPlayer, MatchResult)
from screens.tournaments.register_player import TournamentRegisterPlayer 


class App:
    """The main controller for the club management program"""

    SCREENS = {
        "main-menu": MainMenu,
        "club-create": ClubCreate,
        "club-view": ClubView,
        "player-view": PlayerView,
        "player-edit": PlayerEdit,
        "player-create": PlayerEdit,
        "tournament-create": TournamentCreate,
        "tournament-list": TournamentList,
        "tournament-view": TournamentView,
        "tournament-standings": TournamentStandings,
        "tournament-report": TournamentReport,
        "tournament-results": TournamentResults,
        "match-result": MatchResult,
        "tournament-select-club": TournamentSelectClub,
        "tournament-register-player": TournamentRegisterPlayer,
        "exit": False,}

    def __init__(self):
        # We start with the list of clubs (= main menu)
        command = ClubListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
