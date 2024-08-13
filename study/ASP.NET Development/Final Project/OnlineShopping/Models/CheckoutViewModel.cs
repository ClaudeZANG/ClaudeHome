using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace OnlineShopping.Models
{
    public class CheckoutViewModel
    {
        [Required]
        public string ShippingAddress { get; set; }

        [Required]
        public string ContactNumber { get; set; }

        public List<CartItem> CartItems { get; set; }

        public decimal TotalPrice { get; set; }
    }
}
