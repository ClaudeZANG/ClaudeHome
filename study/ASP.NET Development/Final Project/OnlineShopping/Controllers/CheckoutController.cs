using System;
using System.Linq;
using System.Web.Mvc;
using OnlineShopping.Models;
using Microsoft.AspNet.Identity;

namespace OnlineShopping.Controllers
{
    public class CheckoutController : Controller
    {
        private readonly ApplicationDbContext db = new ApplicationDbContext();

        // GET: Checkout
        public ActionResult Index()
        {
            var userId = User.Identity.GetUserId(); // 获取用户ID
            var cartItems = db.CartItems.Where(c => c.CartId == userId).ToList();
            if (cartItems == null || !cartItems.Any())
            {
                return RedirectToAction("Index", "Cart");
            }

            var model = new CheckoutViewModel
            {
                CartItems = cartItems,
                TotalPrice = cartItems.Sum(c => c.Price * c.Quantity)
            };

            return View(model);
        }

        // POST: Checkout
        [HttpPost]
        public ActionResult Index(CheckoutViewModel model)
        {
            var userId = User.Identity.GetUserId(); // 获取用户ID
            if (ModelState.IsValid)
            {
                var order = new Order
                {
                    OrderDate = DateTime.Now,
                    UserId = userId,
                    TotalAmount = model.TotalPrice,
                    ShippingAddress = model.ShippingAddress,
                    ContactNumber = model.ContactNumber,
                    OrderDetails = model.CartItems.Select(item => new OrderDetail
                    {
                        ProductId = item.ProductId,
                        Quantity = item.Quantity,
                        UnitPrice = item.Price
                    }).ToList()
                };

                db.Orders.Add(order);
                db.SaveChanges();

                // 清空购物车
                db.CartItems.RemoveRange(db.CartItems.Where(c => c.CartId == userId));
                db.SaveChanges();

                return RedirectToAction("Success");
            }

            // 重新加载购物车商品
            model.CartItems = db.CartItems.Where(c => c.CartId == userId).ToList();
            model.TotalPrice = model.CartItems.Sum(c => c.Price * c.Quantity);
            return View(model);
        }

        // GET: Checkout/Success
        public ActionResult Success()
        {
            return View();
        }
    }
}
