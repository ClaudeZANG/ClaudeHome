using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace OnlineShopping.Models
{
    public class Category
    {
        public int CategoryId { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }

        public virtual ICollection<Product> Products { get; set; }
    }

}