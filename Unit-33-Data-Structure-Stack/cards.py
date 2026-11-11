import stack as deck

SUITS = ("Heart - Red", "Diamond - Red", "Club - Black", "Spade - Black")
NUMBERS = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")

def main():
    # Create 52 cards (tuples) into a deck (stack)
    for suit in SUITS:
        for number in NUMBERS:
                        # a card is a string
            # deck.push(f"{number} of {suit}")
                        # better a tuple, cards never change
            deck.push((suit, f"{number}"))

    # Pop each card from the deck
    for i in range(deck.size()):
        # Unpack the tuple
        suit, number = deck.pop()

        # Format the output
        print(f"{i + 1} - {number} of {suit}")
        

if __name__ == "__main__":
    main()