from managers import BJM


def main():
    game = BJM()
    appOn = True

    while appOn:
        appOn = game.play_game()


if __name__ == "__main__":
    main()