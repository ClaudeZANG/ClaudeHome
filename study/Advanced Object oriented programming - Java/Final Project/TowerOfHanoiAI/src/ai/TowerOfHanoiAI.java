package ai;

public class TowerOfHanoiAI {
    public void solveHanoi(int n, char fromPeg, char toPeg, char auxPeg) {
        if (n == 1) {
            System.out.println("Move disk 1 from peg " + fromPeg + " to peg " + toPeg);
            return;
        }
        solveHanoi(n - 1, fromPeg, auxPeg, toPeg);
        System.out.println("Move disk " + n + " from peg " + fromPeg + " to peg " + toPeg);
        solveHanoi(n - 1, auxPeg, toPeg, fromPeg);
    }
}
