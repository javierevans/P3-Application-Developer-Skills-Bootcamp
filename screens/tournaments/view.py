from commands import ClubListCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed when viewing a Tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("Name:", self.tournament.name)
        print("Location:", self.tournament.location)
        print("Start Date:", self.tournament.start_date)
        print("End Date:", self.tournament.end_date)
        print("Description:", self.tournament.description)
        print("Rounds:", self.tournament.number_of_rounds)

    def get_command(self):
        input("\nPress Enter to return...")
        return ClubListCmd()
    
    
    
    