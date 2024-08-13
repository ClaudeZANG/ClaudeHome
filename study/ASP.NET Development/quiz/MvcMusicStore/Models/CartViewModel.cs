using System.Collections.Generic;

namespace MvcMusicStore.Models
{
    public class CartViewModel
    {
        public List<CartItem> CartItems { get; set; }
        public decimal TotalPrice { get; set; }
    }
}
