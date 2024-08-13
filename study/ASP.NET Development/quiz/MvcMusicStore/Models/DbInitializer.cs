using Microsoft.EntityFrameworkCore;
using System.Linq;

namespace MvcMusicStore.Models
{
    public static class DbInitializer
    {
        public static void Initialize(ApplicationDbContext context)
        {
            context.Database.EnsureCreated();

            // 检查是否已有数据
            if (context.Albums.Any())
            {
                return;   // 已初始化
            }

            var albums = new Album[]
            {
            new Album { Title = "Album1", GenreId = 1, ArtistId = 1, Price = 9.99M, AlbumArtUrl = "/images/album1.jpg", Description = "Description1" },
            new Album { Title = "Album2", GenreId = 2, ArtistId = 2, Price = 9.99M, AlbumArtUrl = "/images/album2.jpg", Description = "Description2" },
                // 添加更多 Album
            };

            foreach (Album a in albums)
            {
                context.Albums.Add(a);
            }
            context.SaveChanges();
        }
    }

}
