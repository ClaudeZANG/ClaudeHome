namespace ATMSimulator
{
    public class SavingsAccount : Account
    {
        private readonly decimal interestRate = 0.01m;

        public SavingsAccount(string customerId, string accountNumber, decimal initialBalance)
            : base(customerId, accountNumber, initialBalance)
        {
        }

        public void PayInterest()
        {
            Deposit(AccountBalance * interestRate);
        }
    }
}
