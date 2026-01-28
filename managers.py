from random import randint
from time import sleep
from deck import Deck
from players import HumanBJPlayer, BJPlayer


class BJM:

    COMPNAMES = ["Angela", "Chelsea", "Daryl", "Elizabeth", "Fred", "Gabby",
                 "Harold", "Irene", "Julie", "Katie", "Lindsey", "Mike",
                 "Nancy", "Oliver", "Pat", "Richard", "Samantha", "Terrence",
                 "Ursula", "Vic", "Wendy", "Xavier", "Yanni", "Zach"]

    def __init__(self):
        self.reset()


    def reset(self):
        self.deck = Deck()
        self.dealer = BJPlayer(name="Dealer")
        self.players = {"Computers": [self.dealer],
                        "Humans": []}
        self.scores = {}
        self.winners = []


    def starterDeal(self):
        for _ in range(2):
            for player in self.players["Computers"]:
                player.drawCard(self.deck.draw())
            for player in self.players["Humans"]:
                player.drawCard(self.deck.draw())


    def calculateScore(self, player):
        player.calcScore()
        self.scores[player.name] = player.giveScore()


    def promptNextGame(self):
        self.reset()
        print("Would you like to play another game? (y/n)")
        choice = input(" --> ").lower()
        if choice == 'y' or choice == "yes":
            return True
        return False


    def manageTurn(self, player):
        play = True
        while play:
            print(f"\t~~~~~~~~~~~~~~~ {player}'s Turn ~~~~~~~~~~~~~~~")
            print("")
            player.calcScore()
            playerScore = player.giveScore()
            if playerScore > 21:
                print(f"{player}'s Hand:")
                player.showHand()
                print("")
                print(f"{player.name} busts!\n")
                play = False
            elif len(player.hand) > 5:
                play = False
            else:
                choice = player.makeChoice()
                print("")
                print("")
                print("")
                sleep(1)
                if choice == "hit":
                    player.drawCard(self.deck.draw())
                else:
                    play = False
        self.calculateScore(player)

    
    def determineWinners(self):
        try:
            highScore = max(v for v in self.scores.values() if v <= 21)
            winners = [k for k, v in self.scores.items() if v == highScore]
        except ValueError:
            winners = []
        return winners


    def play_game(self):
        gameOn = True
        while gameOn:

            # Initial setup - currently supports 1 human and multiple computers, with growth potential for more humans
            print("")
            print("")
            print("")
            print("")
            print("")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\t~~~~~~~~~~~~~~~ Welcome to Blackjack!~~~~~~~~~~~~~~~")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            print("")
            print("")
            sleep(1)
            print("What is your name or nickname?")
            playerName = input(" --> ")
            self.players["Humans"].append(HumanBJPlayer(playerName))
            print("")
            print("How many other computers would you like to play against?")
            sleep(1)
            numComps = int(input(" --> "))
            for _ in range(numComps):
                newPlayer = BJPlayer(name=self.COMPNAMES[randint(0, len(self.COMPNAMES) - 1)])
                self.players["Computers"].append(newPlayer)

            # Reverse computer player list so dealer goes last
            self.players["Computers"] = self.players["Computers"][::-1]

            # Initial deck shuffle and deal
            for _ in range(3, 7):
                self.deck.deckShuffle()

            self.starterDeal()

            sleep(1)
            # Show face-up cards
            print("")
            print("")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for player in self.players["Computers"]:
                print(f"{player}'s Hand:")
                player.showHand()
                print("")

            # Manage human player and computer turns
            for playerIdx in range(len(self.players["Humans"])):
                self.manageTurn(self.players["Humans"][playerIdx])
            for playerIdx in range(len(self.players["Computers"])):
                self.manageTurn(self.players["Computers"][playerIdx])

            sleep(1)
            # Determine game winner
            winners = self.determineWinners()
            if len(winners) == 0:
                print("Everbody busts! Nobody wins!")
            elif self.dealer in winners:
                print("The dealer wins! Better luck next time!")
            elif len(winners) == 1:
                print(f"{winners[0]} wins with a score of {self.scores[winners[0]]}!")
            elif len(winners) == 2:
                print(f"{winners[0]} and {winners[1]} both win with a score of {self.scores[winners[0]]}!")
            else:
                winnerNames = ""
                for idx in range(len(winners)):
                    if idx == len(winners) - 1:
                        winnerNames += f" and {winners[idx]} win with a score of {self.scores[winners[0]]}!"
                    else:
                        winnerNames += f"{winners[idx], }"
                print(winnerNames)

            gameOn = self.promptNextGame()
        return False
