from managers import BJM


def main():
    game = BJM()
    appOn = True

    while appOn:
        playGame = input("Would you like to play a game of Blackjack? (Y/N) --> ").upper()
        if playGame == "Y":
            game.play_game()
        else:
            appOn = False


if __name__ == "__main__":
    main()