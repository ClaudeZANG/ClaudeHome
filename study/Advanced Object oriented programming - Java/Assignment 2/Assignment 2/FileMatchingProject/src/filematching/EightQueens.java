package filematching;

public class EightQueens {
    private static final int SIZE = 8;
    private static int[] board = new int[SIZE];

    public static void main(String[] args) {
        solve(0);
        printBoard();
    }

    private static boolean solve(int col) {
        if (col == SIZE) {
            return true;
        }

        for (int row = 0; row < SIZE; row++) {
            if (isSafe(row, col)) {
                board[col] = row;
                if (solve(col + 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    private static boolean isSafe(int row, int col) {
        for (int i = 0; i < col; i++) {
            if (board[i] == row || Math.abs(board[i] - row) == Math.abs(i - col)) {
                return false;
            }
        }
        return true;
    }

    private static void printBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[j] == i) {
                    System.out.print("Q ");
                } else {
                    System.out.print("* ");
                }
            }
            System.out.println();
        }
    }
}
