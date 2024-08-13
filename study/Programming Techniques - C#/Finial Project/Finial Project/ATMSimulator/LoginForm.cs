using System;
using System.Windows.Forms;

namespace ATMSimulator
{
    public partial class LoginForm : Form
    {
        private readonly ATMManager atmManager;

        public LoginForm(ATMManager atmManager)
        {
            InitializeComponent();
            this.atmManager = atmManager;
        }

        private void BtnSubmit_Click(object sender, EventArgs e)
        {
            string name = txtName.Text;
            string pin = txtPIN.Text;

            Customer customer = atmManager.ValidateUser(name, pin);

            if (customer != null)
            {
                this.Hide();
                MainForm mainForm = new MainForm(name, atmManager);
                mainForm.ShowDialog();
                this.Close();
            }
            else
            {
                MessageBox.Show("Invalid credentials. Please try again.");
            }
        }
    }
}
