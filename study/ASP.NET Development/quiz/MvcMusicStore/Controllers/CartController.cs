using Microsoft.AspNetCore.Mvc;
using MvcMusicStore.Models;
using System.Linq;

namespace MvcMusicStore.Controllers
{
    public class CartController : Controller
    {
        private readonly ApplicationDbContext _context;

        public CartController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var cartItems = _context.CartItems.ToList();
            return View(cartItems);
        }
    }
}
