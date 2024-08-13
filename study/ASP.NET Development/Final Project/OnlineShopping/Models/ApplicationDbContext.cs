using System.Data.Entity;
using System.Linq;

namespace OnlineShopping.Models
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext() : base("DefaultConnection") { }

        public DbSet<Product> Products { get; set; }
        public DbSet<CartItem> CartItems { get; set; }
        public DbSet<Order> Orders { get; set; }
        public DbSet<OrderDetail> OrderDetails { get; set; }
        public DbSet<User> Users { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
        }

        public static void InitializeDatabase(ApplicationDbContext context)
        {
            if (!context.Products.Any())
            {
                context.Products.Add(new Product
                {
                    Name = "Sample Product",
                    Description = "This is a sample product.",
                    ImagePath = "~/Images/sample-product.jpg",
                    Price = 9.99M,
                    IsAvailable = true
                });

                context.SaveChanges();
            }
        }
    }
}
