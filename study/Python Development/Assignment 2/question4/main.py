import random

# Function to create a deck of cards.
def create_deck():
    deck = {}
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            # Assign each card a value.
            if value in ['J', 'Q', 'K']:
                deck[value + ' of ' + suit] = 10
            elif value == 'A':
                deck[value + ' of ' + suit] = 11  # Initially consider Ace as 11.
            else:
                deck[value + ' of ' + suit] = int(value)
    return deck

# Function to deal cards to a player.
def deal_card(deck, hand):
    card, value = deck.popitem()
    hand.append((card, value))
    return card, value

# Function to calculate the total value of a hand.
def calculate_hand_value(hand):
    value = sum(card[1] for card in hand)
    # Adjust for Aces if value is greater than 21.
    aces = [card for card in hand if card[0].startswith('A')]
    while value > 21 and aces:
        value -= 10  # Change an Ace's value from 11 to 1.
        aces.pop()
    return value

# Function to play a round of simplified blackjack.
def play_blackjack():
    # Create and shuffle the deck.
    deck = create_deck()
    deck = dict(random.sample(list(deck.items()), len(deck)))  # Shuffle the deck.

    # Initialize players' hands.
    player1_hand = []
    player2_hand = []

    # Deal initial cards.
    deal_card(deck, player1_hand)
    deal_card(deck, player2_hand)
    deal_card(deck, player1_hand)
    deal_card(deck, player2_hand)

    print("\nStarting a new round of blackjack:")
    print("Player 1's initial hand:", player1_hand)
    print("Player 2's initial hand:", player2_hand)

    # Play for Player 1.
    while calculate_hand_value(player1_hand) <= 21:
        print("\nPlayer 1's current hand:", player1_hand)
        if input("Player 1, do you want another card? (y/n): ").lower() == 'y':
            card, value = deal_card(deck, player1_hand)
            print(f"Player 1 was dealt {card}.")
        else:
            break

    player1_value = calculate_hand_value(player1_hand)
    print("\nPlayer 1's final hand:", player1_hand, "with a total value of", player1_value)

    # Play for Player 2.
    while calculate_hand_value(player2_hand) <= 21:
        print("\nPlayer 2's current hand:", player2_hand)
        if input("Player 2, do you want another card? (y/n): ").lower() == 'y':
            card, value = deal_card(deck, player2_hand)
            print(f"Player 2 was dealt {card}.")
        else:
            break

    player2_value = calculate_hand_value(player2_hand)
    print("\nPlayer 2's final hand:", player2_hand, "with a total value of", player2_value)

    # Determine the winner.
    if player1_value > 21 and player2_value > 21:
        print("\nBoth players exceeded 21. No winner.")
    elif player1_value > 21:
        print("\nPlayer 1 exceeded 21. Player 2 wins!")
    elif player2_value > 21:
        print("\nPlayer 2 exceeded 21. Player 1 wins!")
    elif player1_value > player2_value:
        print("\nPlayer 1 wins!")
    elif player2_value > player1_value:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")

def main():
    play_blackjack()

if __name__ == '__main__':
    main()
