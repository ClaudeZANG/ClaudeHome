public class PieceWorker extends Employee {
    private double wage; // wage per piece
    private int pieces; // number of pieces produced

    // Constructor
    public PieceWorker(String firstName, String lastName, String socialSecurityNumber, double wage, int pieces) {
        // Call superclass Employee's constructor
        super(firstName, lastName, socialSecurityNumber);
        this.wage = wage;
        this.pieces = pieces;
    }

    // Getters and setters for wage and pieces
    public double getWage() {
        return wage;
    }

    public void setWage(double wage) {
        this.wage = wage;
    }

    public int getPieces() {
        return pieces;
    }

    public void setPieces(int pieces) {
        this.pieces = pieces;
    }

    // Override toString method
    @Override
    public String toString() {
        // Call superclass Employee's toString method
        return String.format("%s\n%s: %.2f\n%s: %d",
                super.toString(),
                "Wage per piece", getWage(),
                "Pieces produced", getPieces());
    }
}
