namespace ATMSimulator
{
    public class ChequingAccount : Account
    {
        public ChequingAccount(string customerId, string accountNumber, decimal initialBalance)
            : base(customerId, accountNumber, initialBalance)
        {
        }

        public void PayBill(decimal amount)
        {
            base.PayBill(amount);
        }
    }
}
