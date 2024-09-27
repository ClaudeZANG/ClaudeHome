var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseStaticFiles();  // 启用静态文件支持

app.UseRouting();

app.MapGet("/", async context =>
{
    context.Response.Redirect("/index.html");  // 设置默认重定向到 index.html
});

app.Run();
