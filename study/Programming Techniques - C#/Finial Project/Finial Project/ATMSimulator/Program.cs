using System;
using System.Windows.Forms;

namespace ATMSimulator
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            ATMManager atmManager = new ATMManager();
            Application.Run(new LoginForm(atmManager));
        }
    }
}
