using System;
using System.Collections.Generic;
using System.IO;

namespace ATMSimulator
{
    public class ATMManager
    {
        private List<Customer> customers;
        private List<Account> accounts;
        private decimal atmBalance;

        public ATMManager()
        {
            customers = new List<Customer>();
            accounts = new List<Account>();
            atmBalance = 10000m; // Initial ATM balance for demonstration
            LoadCustomers();
            LoadAccounts();
        }

        private void LoadCustomers()
        {
            string[] customerLines = File.ReadAllLines("Customers.txt");
            foreach (var line in customerLines)
            {
                string[] parts = line.Split(',');
                if (parts.Length == 2)
                {
                    string name = parts[0];
                    string pin = parts[1];
                    customers.Add(new Customer(name, pin));
                }
            }
        }

        private void LoadAccounts()
        {
            string[] accountLines = File.ReadAllLines("Accounts.txt");
            foreach (var line in accountLines)
            {
                string[] parts = line.Split(',');
                if (parts.Length == 4)
                {
                    string accountType = parts[0];
                    string customerId = parts[1];
                    string accountNumber = parts[2];
                    decimal balance = decimal.Parse(parts[3]);

                    Account account;
                    if (accountType == "C")
                    {
                        account = new ChequingAccount(customerId, accountNumber, balance);
                    }
                    else
                    {
                        account = new SavingsAccount(customerId, accountNumber, balance);
                    }

                    accounts.Add(account);
                }
            }
        }

        public Customer ValidateUser(string name, string pin)
        {
            foreach (var customer in customers)
            {
                if (customer.Name == name && customer.PIN == pin)
                {
                    return customer;
                }
            }
            return null;
        }

        public void Deposit(decimal amount, string userName, string userPIN)
        {
            var customer = ValidateUser(userName, userPIN);
            if (customer != null)
            {
                var account = GetAccountByCustomer(customer);
                if (account != null)
                {
                    account.Deposit(amount);
                }
            }
        }

        public void Withdraw(decimal amount, string userName, string userPIN)
        {
            var customer = ValidateUser(userName, userPIN);
            if (customer != null)
            {
                var account = GetAccountByCustomer(customer);
                if (account != null && account.AccountBalance >= amount && atmBalance >= amount)
                {
                    account.Withdraw(amount);
                    atmBalance -= amount;
                }
            }
        }

        public void Transfer(decimal amount, string fromUserName, string fromUserPIN, string toUserName, string toUserPIN)
        {
            var fromCustomer = ValidateUser(fromUserName, fromUserPIN);
            var toCustomer = ValidateUser(toUserName, toUserPIN);
            if (fromCustomer != null && toCustomer != null)
            {
                var fromAccount = GetAccountByCustomer(fromCustomer);
                var toAccount = GetAccountByCustomer(toCustomer);
                if (fromAccount != null && toAccount != null && fromAccount.AccountBalance >= amount)
                {
                    fromAccount.Withdraw(amount);
                    toAccount.Deposit(amount);
                }
            }
        }

        public void PayBill(decimal amount, string userName, string userPIN)
        {
            var customer = ValidateUser(userName, userPIN);
            if (customer != null)
            {
                var account = GetAccountByCustomer(customer);
                if (account != null && account.AccountBalance >= amount + 1.25m) // Including bill fee
                {
                    account.PayBill(amount + 1.25m); // Deducting bill fee
                }
            }
        }

        public void PayInterest()
        {
            foreach (var account in accounts)
            {
                if (account is SavingsAccount savingsAccount)
                {
                    savingsAccount.PayInterest();
                }
            }
        }

        public void RefillATM(decimal amount)
        {
            atmBalance += amount;
        }

        public string GetAccountsReport()
        {
            string report = "Account Report:\n";
            foreach (var account in accounts)
            {
                report += $"Account: {account.AccountNumber}, Balance: {account.AccountBalance}\n";
            }
            return report;
        }

        private Account GetAccountByCustomer(Customer customer)
        {
            foreach (var account in accounts)
            {
                if (account.CustomerId == customer.PIN)
                {
                    return account;
                }
            }
            return null;
        }
    }
}
