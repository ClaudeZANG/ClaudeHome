using OnlineShopping.Models;
using System.Linq;
using System.Web.Mvc;

namespace OnlineShopping.Controllers
{
    public class ProductsController : Controller
    {
        private readonly ApplicationDbContext _context;

        public ProductsController()
        {
            _context = new ApplicationDbContext();
        }

        public ActionResult Index()
        {
            var products = _context.Products.ToList();
            return View(products);
        }

        // 其他方法...
    }
}
