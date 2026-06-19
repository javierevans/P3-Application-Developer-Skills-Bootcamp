
class Match:
     def __init__(self, players, completed=False, winner=None):
        if len(players) != 2:
            raise ValueError("A match must have exactly two plyers")
            
            self.players = players
            self.completed = completed 
            self.winner = winner 
            
     def mark_completed(self, winner=None): 
         if winner is not None and winner not in self.players:
             raise ValueError("Winner must be one of teh players in the match")     
         
         self.winner = winner
         self.comlpeted =  True 
         