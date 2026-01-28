from random import randint
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
        self.players = []
        self.scores = {}
        self.winners = []
        self.players.append(self.dealer)
        self.starter_deal()


    def starter_deal(self):
        for _ in range(2):
            for player in self.players:
                player.drawCard(self.deck.draw())


    def calculate_score(self, player):
        player.calcScore()
        self.scores[player.name] = player.giveScore()


    def prompt_nxt_game(self):
        self.reset()
        print("Would you like to play another game? (y/n)")
        choice = input(" --> ").lower()
        if choice == 'y' or choice == "yes":
            return True
        return False


    def manage_turn(self, player):
        play = True
        while play:
            playerScore = player.giveScore()
            if playerScore > 21:
                player.showHand()
                print(f"{player.name} busts!\n")
                play = False
            elif len(player.hand) > 5:
                play = False
            else:
                choice = player.makeChoice()
                if choice == "hit":
                    player.drawCard(self.deck.draw())
                else:
                    play = False
        self.calculate_score(player)


    def play_game(self):
        gameOn = True
        while gameOn:
            print("Welcome to Blackjack!\n")
            print("What is your name or nickname?")
            playerName = input(" --> ")
            self.players.append(HumanBJPlayer(playerName))

            print("How many computers would you like to play against?")
            numComps = int(input(" --> "))
            for _ in range(numComps - 1):
                newPlayer = BJPlayer(name=self.COMPNAMES[randint(0, len(self.COMPNAMES) - 1)])
                self.players.append(newPlayer)

            for _ in range(3, 7):
                self.deck.deckShuffle()

            self.starter_deal()

            for playerIdx in range(1, len(self.players)):
                self.manage_turn(self.players[playerIdx])
            self.manage_turn(self.players[0])

            if self.scores["Dealer"] == 21:
                print("The dealer wins! Better luck next time!")
            else:
                highScore = -1
                for player in self.scores:
                    # This needs to be fixed, adds any player to winners as long as they have higher score than last checked
                    if self.scores[player] > highScore and self.scores[player] < 22:
                        highScore = self.scores[player]
                if self.scores["Dealer"] == highScore:
                    self.winners.append(self.dealer)
                else:
                    for player in self.scores:
                        if self.scores[player] == highScore:
                            self.winners.append(player)

                if len(self.winners) == 0:
                    print("Everyone busted! Nobody wins!")
                elif len(self.winners) > 1:
                    winners = ", ".join([str(player) for player in self.winners])
                    print(f"{winners} win!")
                else:
                    print(f"{self.winners[0]} wins!")

            gameOn = self.prompt_nxt_game()
