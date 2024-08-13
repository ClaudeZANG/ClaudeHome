using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace OnlineShopping.Models
{
    public class ShoppingCart
    {
        ApplicationDbContext db = new ApplicationDbContext();
        string ShoppingCartId { get; set; }

        public static ShoppingCart GetCart(HttpContextBase context)
        {
            var cart = new ShoppingCart();
            cart.ShoppingCartId = cart.GetCartId(context);
            return cart;
        }

        public string GetCartId(HttpContextBase context)
        {
            if (context.Session["CartId"] == null)
            {
                if (!string.IsNullOrWhiteSpace(context.User.Identity.Name))
                {
                    context.Session["CartId"] = context.User.Identity.Name;
                }
                else
                {
                    Guid tempCartId = Guid.NewGuid();
                    context.Session["CartId"] = tempCartId.ToString();
                }
            }
            return context.Session["CartId"].ToString();
        }

        public void AddToCart(Product product)
        {
            var cartItem = db.CartItems.SingleOrDefault(
                c => c.CartId == ShoppingCartId && c.ProductId == product.ProductId);

            if (cartItem == null)
            {
                cartItem = new CartItem
                {
                    ProductId = product.ProductId,
                    CartId = ShoppingCartId,
                    Quantity = 1,
                    Price = product.Price
                };
                db.CartItems.Add(cartItem);
            }
            else
            {
                cartItem.Quantity++;
            }

            db.SaveChanges();
        }

        public int RemoveFromCart(int id)
        {
            var cartItem = db.CartItems.Single(
                cart => cart.CartId == ShoppingCartId && cart.CartItemId == id);

            int itemCount = 0;

            if (cartItem != null)
            {
                if (cartItem.Quantity > 1)
                {
                    cartItem.Quantity--;
                    itemCount = cartItem.Quantity;
                }
                else
                {
                    db.CartItems.Remove(cartItem);
                }
                db.SaveChanges();
            }

            return itemCount;
        }

        public List<CartItem> GetCartItems()
        {
            return db.CartItems.Where(cart => cart.CartId == ShoppingCartId).ToList();
        }

        public decimal GetTotal()
        {
            decimal? total = (from cartItems in db.CartItems
                              where cartItems.CartId == ShoppingCartId
                              select (int?)cartItems.Quantity * cartItems.Price).Sum();

            return total ?? decimal.Zero;
        }

        public void EmptyCart()
        {
            var cartItems = db.CartItems.Where(cart => cart.CartId == ShoppingCartId);

            foreach (var cartItem in cartItems)
            {
                db.CartItems.Remove(cartItem);
            }
            db.SaveChanges();
        }
    }
}
