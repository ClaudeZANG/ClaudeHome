public class SavingsAccount {
    private static double annualInterestRate; // static variable to store annual interest rate
    private double savingsBalance; // instance variable to store the balance

    // Constructor to initialize savings balance
    public SavingsAccount(double savingsBalance) {
        this.savingsBalance = savingsBalance;
    }

    // Method to calculate monthly interest and add it to the balance
    public void calculateMonthlyInterest() {
        double monthlyInterest = (savingsBalance * annualInterestRate) / 12;
        savingsBalance += monthlyInterest;
    }

    // Static method to modify the annual interest rate
    public static void modifyInterestRate(double newInterestRate) {
        annualInterestRate = newInterestRate;
    }

    // Method to get the current balance
    public double getSavingsBalance() {
        return savingsBalance;
    }
}
