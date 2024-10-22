import tkinter as tk
from tkinter import messagebox

def calculate_total():
    total = 0
    if oil_change_var.get():
        total += 30
    if lube_job_var.get():
        total += 20
    if radiator_flush_var.get():
        total += 40
    if transmission_flush_var.get():
        total += 100
    if inspection_var.get():
        total += 35
    if muffler_replacement_var.get():
        total += 200
    if tire_rotation_var.get():
        total += 20
    messagebox.showinfo("Total Charges", f"Total Charges: ${total:.2f}")

# 创建主窗口
window = tk.Tk()
window.title("Joe's Automotive Services")

# 创建复选按钮变量
oil_change_var = tk.BooleanVar()
lube_job_var = tk.BooleanVar()
radiator_flush_var = tk.BooleanVar()
transmission_flush_var = tk.BooleanVar()
inspection_var = tk.BooleanVar()
muffler_replacement_var = tk.BooleanVar()
tire_rotation_var = tk.BooleanVar()

# 创建复选按钮
tk.Checkbutton(window, text="Oil Change - $30.00", variable=oil_change_var).pack(anchor='w')
tk.Checkbutton(window, text="Lube Job - $20.00", variable=lube_job_var).pack(anchor='w')
tk.Checkbutton(window, text="Radiator Flush - $40.00", variable=radiator_flush_var).pack(anchor='w')
tk.Checkbutton(window, text="Transmission Flush - $100.00", variable=transmission_flush_var).pack(anchor='w')
tk.Checkbutton(window, text="Inspection - $35.00", variable=inspection_var).pack(anchor='w')
tk.Checkbutton(window, text="Muffler Replacement - $200.00", variable=muffler_replacement_var).pack(anchor='w')
tk.Checkbutton(window, text="Tire Rotation - $20.00", variable=tire_rotation_var).pack(anchor='w')

# 创建按钮来计算总费用
tk.Button(window, text="Display Charges", command=calculate_total).pack()

# 创建退出按钮
tk.Button(window, text="Quit", command=window.quit).pack()

# 启动主循环
window.mainloop()
