package assignment_2;

public class PieceWorker extends Employee {
    private double wagePerPiece;
    private int pieces;

    public PieceWorker(String firstName, String lastName, String socialSecurityNumber, double wagePerPiece, int pieces) {
        super(firstName, lastName, socialSecurityNumber);
        this.wagePerPiece = wagePerPiece;
        this.pieces = pieces;
    }

    @Override
    public double earnings() {
        return wagePerPiece * pieces;
    }

    @Override
    public String toString() {
        return String.format("Piece Worker: %s\nWage per Piece: %.2f\nPieces Produced: %d",
            super.toString(), wagePerPiece, pieces);
    }
}
