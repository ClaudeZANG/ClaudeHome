using System;
using System.Linq;
using System.Web.Mvc;
using OnlineShopping.Models;
using Microsoft.AspNet.Identity;

namespace OnlineShopping.Controllers
{
    public class CartController : Controller
    {
        private readonly ApplicationDbContext db = new ApplicationDbContext();

        // GET: Cart
        public ActionResult Index()
        {
            var userId = User.Identity.GetUserId(); // 获取用户ID
            var cartItems = db.CartItems.Where(c => c.CartId == userId).ToList();

            var model = new CartViewModel
            {
                CartItems = cartItems,
                TotalPrice = cartItems.Sum(c => c.Price * c.Quantity)
            };

            return View(model);
        }

        // 添加商品到购物车
        public ActionResult AddToCart(int productId)
        {
            var userId = User.Identity.GetUserId(); // 获取用户ID
            var cartItem = db.CartItems.SingleOrDefault(c => c.CartId == userId && c.ProductId == productId);

            if (cartItem == null)
            {
                cartItem = new CartItem
                {
                    CartId = userId,
                    ProductId = productId,
                    Quantity = 1,
                    Price = db.Products.Find(productId).Price
                };
                db.CartItems.Add(cartItem);
            }
            else
            {
                cartItem.Quantity++;
            }

            db.SaveChanges();

            return RedirectToAction("Index");
        }

        // 删除购物车中的商品
        public ActionResult RemoveFromCart(int productId)
        {
            var userId = User.Identity.GetUserId(); // 获取用户ID
            var cartItem = db.CartItems.SingleOrDefault(c => c.CartId == userId && c.ProductId == productId);

            if (cartItem != null)
            {
                db.CartItems.Remove(cartItem);
                db.SaveChanges();
            }

            return RedirectToAction("Index");
        }
    }
}
