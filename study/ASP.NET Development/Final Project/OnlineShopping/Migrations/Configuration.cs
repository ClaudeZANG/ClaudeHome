namespace OnlineShopping.Migrations
{
    using OnlineShopping.Models;
    using System.Data.Entity.Migrations;

    internal sealed class Configuration : DbMigrationsConfiguration<OnlineShopping.Models.ApplicationDbContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }

        protected override void Seed(OnlineShopping.Models.ApplicationDbContext context)
        {
            ApplicationDbContext.InitializeDatabase(context);
        }
    }
}
