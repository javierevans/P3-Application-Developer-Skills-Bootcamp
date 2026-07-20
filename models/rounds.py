from .match import Match


class Round:
    """Represents a single round in a tournament."""

    def __init__(self, round_number, matches=None):
        # Store the round number and its matches
        self.round_number = round_number
        self.matches = matches if matches is not None else []

    def add_match(self, match):
        """Add a match to the round."""

        # Make sure only Match objects are added
        if not isinstance(match, Match):
            raise ValueError(
                "Only Match objects can be added to a round."
            )

        self.matches.append(match)

    def is_completed(self):
        """Return True if every match in the round is completed."""

        return all(match.completed for match in self.matches)

    def serialize(self):
        """Convert the round into a dictionary."""

        return {
            "round_number": self.round_number,
            "matches": [
                match.serialize()
                for match in self.matches
            ],
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Round object from a dictionary."""

        matches = [
            Match.from_dict(match_data)
            for match_data in data["matches"]
        ]

        return cls(
            data["round_number"],
            matches,
        )
