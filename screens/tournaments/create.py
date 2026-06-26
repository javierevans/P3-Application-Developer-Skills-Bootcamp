from ..base_screen import BaseScreen
from commands import TournamentCreateCmd

class TournamentCreate(BaseScreen):
    """Screen displayed when creating a tournament"""
    
    display = "## Create Tournament"

    def get_command(self):
        print("Type in the name of the Tournament")
        name = self.input_string()
        print("Type in the location of the Tournament")
        location = self.input_string()
        print("Type in the start date of the Tournament")
        start_date = self.input_string()
        print("Type in the end date of the Tournament")
        end_date = self.input_string()
        print("Type in the description of the Tournament")
        description = self.input_string()
        print("Type in the number of the rounds")
        number_of_rounds = self.input_string()

        return TournamentCreateCmd(name, location, start_date, end_date, number_of_rounds, description)