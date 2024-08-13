import java.util.Random;
import java.util.Scanner;

public class CoinTossing {
    private int headsCount = 0;
    private int tailsCount = 0;
    private Random random = new Random();

    // Method to simulate a coin flip
    public Coin flip() {
        // Generate a random number, either 0 or 1
        int toss = random.nextInt(2);
        // Return HEADS if the number is 0, otherwise return TAILS
        return (toss == 0) ? Coin.HEADS : Coin.TAILS;
    }

    public void tossCoin() {
        Coin result = flip();
        // Increment the appropriate counter
        if (result == Coin.HEADS) {
            headsCount++;
            System.out.println("Result: HEADS");
        } else {
            tailsCount++;
            System.out.println("Result: TAILS");
        }
    }

    public void displayResults() {
        System.out.println("Heads count: " + headsCount);
        System.out.println("Tails count: " + tailsCount);
    }

    public static void main(String[] args) {
        CoinTossing coinTossing = new CoinTossing();
        Scanner scanner = new Scanner(System.in);
        boolean continueTossing = true;

        while (continueTossing) {
            System.out.println("Choose an option:");
            System.out.println("1. Toss Coin");
            System.out.println("2. Display Results");
            System.out.println("3. Exit");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    coinTossing.tossCoin();
                    break;
                case 2:
                    coinTossing.displayResults();
                    break;
                case 3:
                    continueTossing = false;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
        scanner.close();
    }
}
