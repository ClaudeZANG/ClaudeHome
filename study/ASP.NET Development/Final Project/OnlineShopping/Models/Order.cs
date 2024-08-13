using System.Collections.Generic;
using System;

namespace OnlineShopping.Models
{
    public class Order
    {
        public int OrderId { get; set; }
        public DateTime OrderDate { get; set; }
        public string UserId { get; set; }
        public decimal TotalAmount { get; set; }
        public string ShippingAddress { get; set; }
        public string ContactNumber { get; set; }

        public virtual ICollection<OrderDetail> OrderDetails { get; set; }
    }
}
