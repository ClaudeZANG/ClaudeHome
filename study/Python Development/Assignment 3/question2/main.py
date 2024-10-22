import tkinter as tk
from tkinter import messagebox


def calculate_tax():
    try:
        # 获取用户输入的实际房产价值
        actual_value = float(entry_actual_value.get())

        # 计算评估价值（60% 的实际价值）
        assessed_value = actual_value * 0.6

        # 计算房产税（每 $100 评估价值需缴纳 $0.75）
        property_tax = (assessed_value / 100) * 0.75

        # 显示评估价值和房产税
        label_result.config(
            text=f"Assessed Value: ${assessed_value:.2f}\nProperty Tax: ${property_tax:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the property value.")


# 创建主窗口
window = tk.Tk()
window.title("Property Tax Calculator")

# 创建输入标签和输入框
tk.Label(window, text="Enter the actual property value:").pack(pady=5)
entry_actual_value = tk.Entry(window)
entry_actual_value.pack(pady=5)

# 创建按钮来计算税额
tk.Button(window, text="Calculate Tax", command=calculate_tax).pack(pady=5)

# 显示结果的标签
label_result = tk.Label(window, text="")
label_result.pack(pady=10)

# 创建退出按钮
tk.Button(window, text="Quit", command=window.quit).pack(pady=5)

# 启动主循环
window.mainloop()
