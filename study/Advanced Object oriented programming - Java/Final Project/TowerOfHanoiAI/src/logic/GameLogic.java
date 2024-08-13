package logic;

public class GameLogic {
    private int numDisks = 3; // Number of disks

    public void startGame() {
        // Implement game logic here
        System.out.println("Game started!");
        moveDisks(numDisks, 'A', 'C', 'B');
    }

    private void moveDisks(int n, char fromPeg, char toPeg, char auxPeg) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + fromPeg + " to " + toPeg);
            return;
        }
        moveDisks(n - 1, fromPeg, auxPeg, toPeg);
        System.out.println("Move disk " + n + " from " + fromPeg + " to " + toPeg);
        moveDisks(n - 1, auxPeg, toPeg, fromPeg);
    }
}
