using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MvcMusicStore.Models;
using System.Linq;

namespace MvcMusicStore.Controllers
{
    public class StoreController : Controller
    {
        private readonly ApplicationDbContext _context;

        public StoreController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var genres = _context.Genres.ToList();
            return View(genres);
        }

        public IActionResult Browse(string genre)
        {
            var genreModel = _context.Genres.Include("Albums").Single(g => g.Name == genre);
            return View(genreModel);
        }

        public IActionResult Details(int id)
        {
            var album = _context.Albums.Find(id);
            return View(album);
        }
    }
}
