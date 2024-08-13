namespace ATMSimulator
{
    public class Account
    {
        public string CustomerId { get; set; }
        public string AccountNumber { get; set; }
        public decimal AccountBalance { get; private set; }

        public Account(string customerId, string accountNumber, decimal initialBalance)
        {
            CustomerId = customerId;
            AccountNumber = accountNumber;
            AccountBalance = initialBalance;
        }

        public void Deposit(decimal amount)
        {
            AccountBalance += amount;
        }

        public void Withdraw(decimal amount)
        {
            if (AccountBalance >= amount)
            {
                AccountBalance -= amount;
            }
        }

        public void PayBill(decimal amount)
        {
            if (AccountBalance >= amount)
            {
                AccountBalance -= amount;
            }
        }
    }
}
