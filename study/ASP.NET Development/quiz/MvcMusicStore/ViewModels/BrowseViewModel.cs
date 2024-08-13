using MvcMusicStore.Models;

namespace MvcMusicStore.ViewModels
{
    public class BrowseViewModel
    {
        public Genre Genre { get; set; }
        public List<Album> Albums { get; set; }
    }
}
