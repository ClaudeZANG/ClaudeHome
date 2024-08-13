package assignment_1;

public class Invoice {
    // Instance variables
    private String partNumber;
    private String partDescription;
    private int quantity;
    private double pricePerItem;

    // Constructor to initialize instance variables
    public Invoice(String partNumber, String partDescription, int quantity, double pricePerItem) {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        this.quantity = (quantity > 0) ? quantity : 0; // Ensure quantity is not negative
        this.pricePerItem = (pricePerItem > 0) ? pricePerItem : 0.0; // Ensure price is not negative
    }

    // Set and get methods for partNumber
    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }

    public String getPartNumber() {
        return partNumber;
    }

    // Set and get methods for partDescription
    public void setPartDescription(String partDescription) {
        this.partDescription = partDescription;
    }

    public String getPartDescription() {
        return partDescription;
    }

    // Set and get methods for quantity
    public void setQuantity(int quantity) {
        this.quantity = (quantity > 0) ? quantity : 0;
    }

    public int getQuantity() {
        return quantity;
    }

    // Set and get methods for pricePerItem
    public void setPricePerItem(double pricePerItem) {
        this.pricePerItem = (pricePerItem > 0) ? pricePerItem : 0.0;
    }

    public double getPricePerItem() {
        return pricePerItem;
    }

    // Method to calculate the invoice amount
    public double getInvoiceAmount() {
        return quantity * pricePerItem;
    }
}
