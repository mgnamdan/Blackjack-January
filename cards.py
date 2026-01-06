class Card:

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit

    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

    def __eq__(self, other):
        if isinstance(other, Card):
            if self.rank == other.rank and self.suit == other.suit:
                return True
            else:
                return False
        else:
            return False