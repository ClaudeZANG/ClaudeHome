public class SavingsAccountTester {
    public static void main(String[] args) {
        // Instantiate two SavingsAccount objects
        SavingsAccount saver1 = new SavingsAccount(2000.00);
        SavingsAccount saver2 = new SavingsAccount(3000.00);

        // Set the annual interest rate to 4%
        SavingsAccount.modifyInterestRate(0.04);

        // Calculate and print the new balances for each of 12 months
        System.out.println("Monthly balances for one year at 4% annual interest rate:");
        for (int month = 1; month <= 12; month++) {
            saver1.calculateMonthlyInterest();
            saver2.calculateMonthlyInterest();
            System.out.printf("Month %d: Saver 1: $%.2f, Saver 2: $%.2f%n", month, saver1.getSavingsBalance(), saver2.getSavingsBalance());
        }

        // Set the annual interest rate to 5%
        SavingsAccount.modifyInterestRate(0.05);

        // Calculate and print the next month's balances
        saver1.calculateMonthlyInterest();
        saver2.calculateMonthlyInterest();
        System.out.println("\nBalances after one month at 5% annual interest rate:");
        System.out.printf("Saver 1: $%.2f, Saver 2: $%.2f%n", saver1.getSavingsBalance(), saver2.getSavingsBalance());
    }
}
