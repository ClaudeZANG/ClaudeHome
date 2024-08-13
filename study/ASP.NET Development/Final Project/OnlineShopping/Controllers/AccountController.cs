using System.Linq;
using System.Web.Mvc;
using OnlineShopping.Models;

namespace OnlineShopping.Controllers
{
    public class AccountController : Controller
    {
        private readonly ApplicationDbContext db = new ApplicationDbContext();

        // GET: Account/Login
        public ActionResult Login()
        {
            return View();
        }

        // POST: Account/Login
        [HttpPost]
        public ActionResult Login(LoginViewModel model)
        {
            if (ModelState.IsValid)
            {
                var user = db.Users.FirstOrDefault(u => u.Username == model.Username && u.Password == model.Password);
                if (user != null)
                {
                    Session["User"] = user.Username;
                    return RedirectToAction("Index", "Home");
                }
                ModelState.AddModelError("", "用户名或密码无效");
            }
            return View(model);
        }

        // GET: Account/Register
        public ActionResult Register()
        {
            return View();
        }

        // POST: Account/Register
        [HttpPost]
        public ActionResult Register(RegisterViewModel model)
        {
            if (ModelState.IsValid)
            {
                var user = new User { Username = model.Username, Password = model.Password, Email = model.Email, IsAdmin = false };
                db.Users.Add(user);
                db.SaveChanges();
                return RedirectToAction("Login");
            }
            return View(model);
        }

        public ActionResult Logout()
        {
            Session["User"] = null;
            return RedirectToAction("Login");
        }
    }
}
