using System;
using System.Windows.Forms;

namespace ATMSimulator
{
    public partial class MainForm : Form
    {
        private readonly ATMManager _atmManager;
        private readonly string _currentUserName;

        public MainForm(string userName, ATMManager atmManager)
        {
            InitializeComponent();
            _atmManager = atmManager;
            _currentUserName = userName;
        }

        private void BtnSubmit_Click(object sender, EventArgs e)
        {
            string targetName = txtTargetName.Text;
            string targetPIN = txtTargetPIN.Text;
            decimal amount;

            if (decimal.TryParse(txtAmount.Text, out amount))
            {
                if (rdoDeposit.Checked)
                {
                    _atmManager.Deposit(amount, _currentUserName, _currentUserName);
                    lblResult.Text = "Deposit successful.";
                }
                else if (rdoWithdraw.Checked)
                {
                    _atmManager.Withdraw(amount, _currentUserName, _currentUserName);
                    lblResult.Text = "Withdraw successful.";
                }
                else if (rdoTransfer.Checked)
                {
                    _atmManager.Transfer(amount, _currentUserName, _currentUserName, targetName, targetPIN);
                    lblResult.Text = "Transfer successful.";
                }
                else if (rdoPayBill.Checked)
                {
                    _atmManager.PayBill(amount, _currentUserName, _currentUserName);
                    lblResult.Text = "Bill payment successful.";
                }
            }
            else
            {
                lblResult.Text = "Invalid amount.";
            }
        }
    }
}
