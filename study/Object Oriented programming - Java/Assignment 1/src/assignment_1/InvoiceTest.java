package assignment_1;

public class InvoiceTest {
    public static void main(String[] args) {
        // Create an Invoice object
        Invoice invoice = new Invoice("1234", "Hammer", 2, 19.95);

        // Display the part number, description, quantity, and price per item
        System.out.printf("Part Number: %s%n", invoice.getPartNumber());
        System.out.printf("Part Description: %s%n", invoice.getPartDescription());
        System.out.printf("Quantity: %d%n", invoice.getQuantity());
        System.out.printf("Price per Item: %.2f%n", invoice.getPricePerItem());

        // Display the invoice amount
        System.out.printf("Invoice Amount: %.2f%n", invoice.getInvoiceAmount());
    }
}
