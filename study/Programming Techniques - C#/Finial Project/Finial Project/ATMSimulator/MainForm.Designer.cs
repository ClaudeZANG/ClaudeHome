namespace ATMSimulator
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.RadioButton rdoChequing;
        private System.Windows.Forms.RadioButton rdoSavings;
        private System.Windows.Forms.RadioButton rdoDeposit;
        private System.Windows.Forms.RadioButton rdoWithdraw;
        private System.Windows.Forms.RadioButton rdoTransfer;
        private System.Windows.Forms.RadioButton rdoPayBill;
        private System.Windows.Forms.TextBox txtAmount;
        private System.Windows.Forms.TextBox txtTargetName;
        private System.Windows.Forms.TextBox txtTargetPIN;
        private System.Windows.Forms.Label lblResult;
        private System.Windows.Forms.Button btnSubmit;

        private void InitializeComponent()
        {
            this.rdoChequing = new System.Windows.Forms.RadioButton();
            this.rdoSavings = new System.Windows.Forms.RadioButton();
            this.rdoDeposit = new System.Windows.Forms.RadioButton();
            this.rdoWithdraw = new System.Windows.Forms.RadioButton();
            this.rdoTransfer = new System.Windows.Forms.RadioButton();
            this.rdoPayBill = new System.Windows.Forms.RadioButton();
            this.txtAmount = new System.Windows.Forms.TextBox();
            this.txtTargetName = new System.Windows.Forms.TextBox();
            this.txtTargetPIN = new System.Windows.Forms.TextBox();
            this.lblResult = new System.Windows.Forms.Label();
            this.btnSubmit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // rdoChequing
            // 
            this.rdoChequing.AutoSize = true;
            this.rdoChequing.Location = new System.Drawing.Point(35, 35);
            this.rdoChequing.Name = "rdoChequing";
            this.rdoChequing.Size = new System.Drawing.Size(78, 17);
            this.rdoChequing.TabIndex = 0;
            this.rdoChequing.TabStop = true;
            this.rdoChequing.Text = "Chequing";
            this.rdoChequing.UseVisualStyleBackColor = true;
            // 
            // rdoSavings
            // 
            this.rdoSavings.AutoSize = true;
            this.rdoSavings.Location = new System.Drawing.Point(35, 65);
            this.rdoSavings.Name = "rdoSavings";
            this.rdoSavings.Size = new System.Drawing.Size(63, 17);
            this.rdoSavings.TabIndex = 1;
            this.rdoSavings.TabStop = true;
            this.rdoSavings.Text = "Savings";
            this.rdoSavings.UseVisualStyleBackColor = true;
            // 
            // rdoDeposit
            // 
            this.rdoDeposit.AutoSize = true;
            this.rdoDeposit.Location = new System.Drawing.Point(35, 95);
            this.rdoDeposit.Name = "rdoDeposit";
            this.rdoDeposit.Size = new System.Drawing.Size(62, 17);
            this.rdoDeposit.TabIndex = 2;
            this.rdoDeposit.TabStop = true;
            this.rdoDeposit.Text = "Deposit";
            this.rdoDeposit.UseVisualStyleBackColor = true;
            // 
            // rdoWithdraw
            this.rdoWithdraw.AutoSize = true;
            this.rdoWithdraw.Location = new System.Drawing.Point(35, 125);
            this.rdoWithdraw.Name = "rdoWithdraw";
            this.rdoWithdraw.Size = new System.Drawing.Size(70, 17);
            this.rdoWithdraw.TabIndex = 3;
            this.rdoWithdraw.TabStop = true;
            this.rdoWithdraw.Text = "Withdraw";
            this.rdoWithdraw.UseVisualStyleBackColor = true;
            // 
            // rdoTransfer
            // 
            this.rdoTransfer.AutoSize = true;
            this.rdoTransfer.Location = new System.Drawing.Point(35, 155);
            this.rdoTransfer.Name = "rdoTransfer";
            this.rdoTransfer.Size = new System.Drawing.Size(65, 17);
            this.rdoTransfer.TabIndex = 4;
            this.rdoTransfer.TabStop = true;
            this.rdoTransfer.Text = "Transfer";
            this.rdoTransfer.UseVisualStyleBackColor = true;
            // 
            // rdoPayBill
            // 
            this.rdoPayBill.AutoSize = true;
            this.rdoPayBill.Location = new System.Drawing.Point(35, 185);
            this.rdoPayBill.Name = "rdoPayBill";
            this.rdoPayBill.Size = new System.Drawing.Size(58, 17);
            this.rdoPayBill.TabIndex = 5;
            this.rdoPayBill.TabStop = true;
            this.rdoPayBill.Text = "Pay Bill";
            this.rdoPayBill.UseVisualStyleBackColor = true;
            // 
            // txtAmount
            // 
            this.txtAmount.Location = new System.Drawing.Point(150, 35);
            this.txtAmount.Name = "txtAmount";
            this.txtAmount.Size = new System.Drawing.Size(100, 20);
            this.txtAmount.TabIndex = 6;
            // 
            // txtTargetName
            // 
            this.txtTargetName.Location = new System.Drawing.Point(150, 65);
            this.txtTargetName.Name = "txtTargetName";
            this.txtTargetName.Size = new System.Drawing.Size(100, 20);
            this.txtTargetName.TabIndex = 7;
            // 
            // txtTargetPIN
            // 
            this.txtTargetPIN.Location = new System.Drawing.Point(150, 95);
            this.txtTargetPIN.Name = "txtTargetPIN";
            this.txtTargetPIN.Size = new System.Drawing.Size(100, 20);
            this.txtTargetPIN.TabIndex = 8;
            // 
            // lblResult
            // 
            this.lblResult.AutoSize = true;
            this.lblResult.Location = new System.Drawing.Point(35, 215);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(37, 13);
            this.lblResult.TabIndex = 9;
            this.lblResult.Text = "Result";
            // 
            // btnSubmit
            // 
            this.btnSubmit.Location = new System.Drawing.Point(150, 125);
            this.btnSubmit.Name = "btnSubmit";
            this.btnSubmit.Size = new System.Drawing.Size(75, 23);
            this.btnSubmit.TabIndex = 10;
            this.btnSubmit.Text = "Submit";
            this.btnSubmit.UseVisualStyleBackColor = true;
            this.btnSubmit.Click += new System.EventHandler(this.BtnSubmit_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.btnSubmit);
            this.Controls.Add(this.lblResult);
            this.Controls.Add(this.txtTargetPIN);
            this.Controls.Add(this.txtTargetName);
            this.Controls.Add(this.txtAmount);
            this.Controls.Add(this.rdoPayBill);
            this.Controls.Add(this.rdoTransfer);
            this.Controls.Add(this.rdoWithdraw);
            this.Controls.Add(this.rdoDeposit);
            this.Controls.Add(this.rdoSavings);
            this.Controls.Add(this.rdoChequing);
            this.Name = "MainForm";
            this.Text = "ATM Simulator";
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
