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
     
     def serialize(self):
         return {
             "round_number" : self.round_number,
             "matches" : [ match.serialize() for match in self.matches],
         }
        
     @classmethod
     def from_dict(cls, data):
         matches = [
             Match.from_dict(match_data)
             for match_data in data["matches"]
         ]
         return cls(
             data["round_number"],
             matches
         )
        
        