using Microsoft.AspNetCore.Mvc;
using MvcMusicStore.Models;

public class HomeController : Controller
{
    private readonly ApplicationDbContext _context;

    public HomeController(ApplicationDbContext context)
    {
        _context = context;
    }

    public IActionResult Index()
    {
        var albums = _context.Albums.ToList();
        return View(albums);
    }
}
