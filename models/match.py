from .player import Player


class Match:
     def __init__(self, players, completed=False, winner=None):
        if len(players) != 2:
            raise ValueError("A match must have exactly two players")
            
        self.players = players
        self.completed = completed 
        self.winner = winner 
            
     def mark_completed(self, winner=None): 
         if winner is not None and winner not in self.players:
             raise ValueError("Winner must be one of the players in the match")     
         
         self.winner = winner
         self.completed =  True 
    
     def serialize(self):
         return{
             "players" : [ player.serialize() for player in self.players],
             "winner" : (self.winner.serialize() if self.winner is not None else None ),
             "completed" : self.completed,
             
         }
         
     @classmethod
     def from_dict(cls, data):
        players = [
        Player.from_dict(player_data)
        for player_data in data["players"]
        ]

        winner = (
        Player.from_dict(data["winner"])
        if data["winner"] is not None
        else None
        )

        return cls(
        players,
        data["completed"],
        winner,
        )