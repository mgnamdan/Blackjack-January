class BJPlayer:
    
    RANKVALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
                  "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
                  "Queen": 10, "King": 10, "Ace": 11}
    
    # hands = {1: [], 2: [], 3: [], 4: []}

    def __init__(self, name="Bob"):
        self.name = name
        self.hand = []
        # self.extraHand = []
        self.score = 0


    def __str__(self):
        return f"{self.name}"


    def __eq__(self):
        pass


    def showHand(self):
        for idx in range(len(self.hand)):
            print(f"{idx+1}. {self.hand[idx]}")


    def giveScore(self):
        return self.score


    def drawCard(self, card):
        self.hand.append(card)


    def discardCard(self, cardIdx):
        returnedCard = self.hand.pop(cardIdx)
        return returnedCard


    def calcScore(self):
        self.score = 0
        if len(self.hand) != 0:
            for card in self.hand:
                self.score += self.RANKVALUES[card.rank]


    def makeChoice(self):
        self.calcScore()
        if self.score > 17:
            return "stay"
        else:
            return "hit"
        


class HumanBJPlayer(BJPlayer):
     
    def __init__(self, name="Bob"):
        super().__init__(name)

    
    def discardCard(self):
        self.showHand()
        idxChoice = int(input("Which card would you like to discard? -> "))
        returnedCard = self.hand.pop(idxChoice-1)
        return returnedCard
    

    def makeChoice(self):
        self.calcScore()
        self.showHand()
        choice = input("Would you like to hit or stay? -> ").lower()
        if choice == "h":
            choice == "hit"
        if choice == "s":
            choice == "stay"
        return choice