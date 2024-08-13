using System;
using System.Windows.Forms;

namespace ATMSimulator
{
    public partial class SupervisorForm : Form
    {
        private readonly ATMManager _atmManager;

        public SupervisorForm(ATMManager atmManager)
        {
            InitializeComponent();
            _atmManager = atmManager;
        }

        private void BtnRefillATM_Click(object sender, EventArgs e)
        {
            decimal amount;
            if (decimal.TryParse(txtRefillAmount.Text, out amount))
            {
                _atmManager.RefillATM(amount);
                lblSupervisorResult.Text = "ATM refilled successfully.";
            }
            else
            {
                lblSupervisorResult.Text = "Invalid amount.";
            }
        }

        private void BtnPayInterest_Click(object sender, EventArgs e)
        {
            _atmManager.PayInterest();
            lblSupervisorResult.Text = "Interest paid to all savings accounts.";
        }

        private void BtnGetAccountsReport_Click(object sender, EventArgs e)
        {
            var report = _atmManager.GetAccountsReport();
            lblSupervisorResult.Text = report;
        }
    }
}
