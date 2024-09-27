var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseStaticFiles();  // ���þ�̬�ļ�֧��

app.UseRouting();

app.MapGet("/", async context =>
{
    context.Response.Redirect("/index.html");  // ����Ĭ���ض��� index.html
});

app.Run();
