from cards import Card


def main():
    cardOne = Card()
    cardTwo = Card("Two", "Clubs")
    cardThree = Card("Two", "Diamonds")
    cardFour = Card("Reverse", "Blue")


    print(cardOne)
    print(cardTwo)
    print(cardThree)
    print(cardFour)




if __name__ == "__main__":
    main()