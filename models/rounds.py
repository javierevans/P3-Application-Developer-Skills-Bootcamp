from .match import Match


class Round:
     def __init__(self, round_number, matches = None):
        
            self.round_number = round_number
            self.matches = matches if matches is not None else []
            
     def add_match(self,match):
         if not isinstance(match,Match):
             raise ValueError("Only Match objects can be added to a round.")
         
         self.matches.append(match)
         
     def is_completed(self):
         return all(match.completed for match in self.matches)