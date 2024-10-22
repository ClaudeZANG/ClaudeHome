import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title("Solar System")

# 创建 Canvas 小部件
canvas = tk.Canvas(window, width=800, height=400, bg="black")
canvas.pack()

# 常量：设置行星的相对半径和距离（简化）
PLANET_RADIUS = {
    "Sun": 30,
    "Mercury": 5,
    "Venus": 8,
    "Earth": 8,
    "Mars": 6,
    "Jupiter": 20,
    "Saturn": 18,
    "Uranus": 14,
    "Neptune": 14,
    "Pluto": 4
}

# 常量：行星的相对距离
PLANET_DISTANCE = {
    "Sun": 50,
    "Mercury": 100,
    "Venus": 150,
    "Earth": 200,
    "Mars": 250,
    "Jupiter": 350,
    "Saturn": 450,
    "Uranus": 550,
    "Neptune": 650,
    "Pluto": 750
}

# 绘制太阳和行星
def draw_planet(name, radius, distance, color):
    x0 = distance
    y0 = 200 - radius
    x1 = distance + 2 * radius
    y1 = 200 + radius
    canvas.create_oval(x0, y0, x1, y1, fill=color)
    canvas.create_text(x0 + radius, y1 + 10, text=name, fill="white")

# 绘制太阳和各个行星
draw_planet("Sun", PLANET_RADIUS["Sun"], PLANET_DISTANCE["Sun"], "yellow")
draw_planet("Mercury", PLANET_RADIUS["Mercury"], PLANET_DISTANCE["Mercury"], "gray")
draw_planet("Venus", PLANET_RADIUS["Venus"], PLANET_DISTANCE["Venus"], "orange")
draw_planet("Earth", PLANET_RADIUS["Earth"], PLANET_DISTANCE["Earth"], "blue")
draw_planet("Mars", PLANET_RADIUS["Mars"], PLANET_DISTANCE["Mars"], "red")
draw_planet("Jupiter", PLANET_RADIUS["Jupiter"], PLANET_DISTANCE["Jupiter"], "brown")
draw_planet("Saturn", PLANET_RADIUS["Saturn"], PLANET_DISTANCE["Saturn"], "gold")
draw_planet("Uranus", PLANET_RADIUS["Uranus"], PLANET_DISTANCE["Uranus"], "lightblue")
draw_planet("Neptune", PLANET_RADIUS["Neptune"], PLANET_DISTANCE["Neptune"], "blue")
draw_planet("Pluto", PLANET_RADIUS["Pluto"], PLANET_DISTANCE["Pluto"], "white")

# 启动主循环
window.mainloop()
