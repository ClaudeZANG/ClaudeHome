import java.util.Random;

public class DeckOfCards {
    private static final int NUMBER_OF_CARDS = 52; // constant number of Cards
    private Card[] deck; // array of Card objects
    private int currentCard; // index of next Card to be dealt
    private static final Random randomNumbers = new Random(); // random number generator

    // constructor fills deck of Cards
    public DeckOfCards() {
        String[] faces = {"Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"};
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};

        deck = new Card[NUMBER_OF_CARDS]; // create array of Card objects
        currentCard = 0; // initialize currentCard

        // populate deck with Card objects
        for (int count = 0; count < deck.length; count++) {
            deck[count] = new Card(faces[count % 13], suits[count / 13]);
        }
    }

    // shuffle deck of Cards with one-pass algorithm
    public void shuffle() {
        currentCard = 0; // reinitialize currentCard

        // for each Card, pick another random Card and swap them
        for (int first = 0; first < deck.length; first++) {
            // select a random number between 0 and 51
            int second = randomNumbers.nextInt(NUMBER_OF_CARDS);

            // swap current Card with randomly selected Card
            Card temp = deck[first];
            deck[first] = deck[second];
            deck[second] = temp;
        }
    }

    // deal one Card
    public Card dealCard() {
        // determine whether Cards remain to be dealt
        if (currentCard < deck.length) {
            return deck[currentCard++]; // return current Card in array
        } else {
            return null; // return null to indicate that all Cards were dealt
        }
    }

    public static void main(String[] args) {
        DeckOfCards deckOfCards = new DeckOfCards();
        deckOfCards.shuffle(); // place Cards in random order

        // print all 52 Cards in the order in which they are dealt
        for (int i = 0; i < NUMBER_OF_CARDS; i++) {
            System.out.printf("%-19s", deckOfCards.dealCard());
            if ((i + 1) % 4 == 0) {
                System.out.println();
            }
        }
    }
}
