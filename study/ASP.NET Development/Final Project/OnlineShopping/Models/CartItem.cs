using System.ComponentModel.DataAnnotations;

namespace OnlineShopping.Models
{
    public class CartItem
    {
        [Key]
        public int CartItemId { get; set; }
        public string CartId { get; set; }
        public int ProductId { get; set; }
        public int Quantity { get; set; }
        public decimal Price { get; set; }

        public virtual Product Product { get; set; }
    }
}
