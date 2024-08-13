namespace ATMSimulator
{
    partial class SupervisorForm
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.Button btnRefillATM;
        private System.Windows.Forms.Button btnPayInterest;
        private System.Windows.Forms.Button btnGetAccountsReport;
        private System.Windows.Forms.TextBox txtRefillAmount;
        private System.Windows.Forms.Label lblSupervisorResult;

        private void InitializeComponent()
        {
            this.btnRefillATM = new System.Windows.Forms.Button();
            this.btnPayInterest = new System.Windows.Forms.Button();
            this.btnGetAccountsReport = new System.Windows.Forms.Button();
            this.txtRefillAmount = new System.Windows.Forms.TextBox();
            this.lblSupervisorResult = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnRefillATM
            // 
            this.btnRefillATM.Location = new System.Drawing.Point(12, 12);
            this.btnRefillATM.Name = "btnRefillATM";
            this.btnRefillATM.Size = new System.Drawing.Size(100, 23);
            this.btnRefillATM.TabIndex = 0;
            this.btnRefillATM.Text = "Refill ATM";
            this.btnRefillATM.UseVisualStyleBackColor = true;
            this.btnRefillATM.Click += new System.EventHandler(this.BtnRefillATM_Click);
            // 
            // btnPayInterest
            // 
            this.btnPayInterest.Location = new System.Drawing.Point(12, 41);
            this.btnPayInterest.Name = "btnPayInterest";
            this.btnPayInterest.Size = new System.Drawing.Size(100, 23);
            this.btnPayInterest.TabIndex = 1;
            this.btnPayInterest.Text = "Pay Interest";
            this.btnPayInterest.UseVisualStyleBackColor = true;
            this.btnPayInterest.Click += new System.EventHandler(this.BtnPayInterest_Click);
            // 
            // btnGetAccountsReport
            // 
            this.btnGetAccountsReport.Location = new System.Drawing.Point(12, 70);
            this.btnGetAccountsReport.Name = "btnGetAccountsReport";
            this.btnGetAccountsReport.Size = new System.Drawing.Size(100, 23);
            this.btnGetAccountsReport.TabIndex = 2;
            this.btnGetAccountsReport.Text = "Get Report";
            this.btnGetAccountsReport.UseVisualStyleBackColor = true;
            this.btnGetAccountsReport.Click += new System.EventHandler(this.BtnGetAccountsReport_Click);
            // 
            // txtRefillAmount
            // 
            this.txtRefillAmount.Location = new System.Drawing.Point(118, 14);
            this.txtRefillAmount.Name = "txtRefillAmount";
            this.txtRefillAmount.Size = new System.Drawing.Size(100, 20);
            this.txtRefillAmount.TabIndex = 3;
            // 
            // lblSupervisorResult
            // 
            this.lblSupervisorResult.AutoSize = true;
            this.lblSupervisorResult.Location = new System.Drawing.Point(12, 96);
            this.lblSupervisorResult.Name = "lblSupervisorResult";
            this.lblSupervisorResult.Size = new System.Drawing.Size(37, 13);
            this.lblSupervisorResult.TabIndex = 4;
            this.lblSupervisorResult.Text = "Result";
            // 
            // SupervisorForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.lblSupervisorResult);
            this.Controls.Add(this.txtRefillAmount);
            this.Controls.Add(this.btnGetAccountsReport);
            this.Controls.Add(this.btnPayInterest);
            this.Controls.Add(this.btnRefillATM);
            this.Name = "SupervisorForm";
            this.Text = "Supervisor Form";
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
