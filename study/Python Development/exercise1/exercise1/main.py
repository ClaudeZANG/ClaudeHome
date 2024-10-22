# # Q1:
#
# def display_personal_info():
#     name = "CHUANJIE ZANG"
#     address = "123 Main Street, Vancouver, BC, V5K 0A1"
#     phone_number = "778-895-3789"
#     major = "Python Development"
#
#     print("Personal Information:")
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Phone Number: {phone_number}")
#     print(f"Major: {major}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_personal_info()

# # q2:
#
# def sales_prediction():
#     # 询问用户输入预期的销售总额
#     total_sales = float(input("Enter the projected total sales: $"))
#
#     # 计算利润，23% 的利润率
#     profit = total_sales * 0.23
#
#     # 显示利润
#     print(f"The projected profit is: ${profit:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     sales_prediction()

# # Q3:
#
# def land_calculation():
#     # 每英亩的平方英尺数
#     square_feet_per_acre = 43560
#
#     # 询问用户输入土地的总平方英尺数
#     total_square_feet = float(input("Enter the total square feet in the tract of land: "))
#
#     # 计算英亩数
#     acres = total_square_feet / square_feet_per_acre
#
#     # 显示结果
#     print(f"The land area is: {acres:.2f} acres")
#
#
# # 调用函数
# if __name__ == "__main__":
#     land_calculation()

# # Q4:
# def total_purchase():
#     # 定义销售税率
#     sales_tax_rate = 0.07
#
#     # 询问用户输入五件物品的价格
#     item1 = float(input("Enter the price of item 1: $"))
#     item2 = float(input("Enter the price of item 2: $"))
#     item3 = float(input("Enter the price of item 3: $"))
#     item4 = float(input("Enter the price of item 4: $"))
#     item5 = float(input("Enter the price of item 5: $"))
#
#     # 计算小计
#     subtotal = item1 + item2 + item3 + item4 + item5
#
#     # 计算销售税
#     sales_tax = subtotal * sales_tax_rate
#
#     # 计算总金额
#     total = subtotal + sales_tax
#
#     # 显示结果
#     print(f"Subtotal: ${subtotal:.2f}")
#     print(f"Sales Tax: ${sales_tax:.2f}")
#     print(f"Total: ${total:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     total_purchase()

# # Q5:
#
# def distance_traveled():
#     # 汽车的速度（每小时英里数）
#     speed = 70
#
#     # 计算不同时间下的行驶距离
#     distance_6_hours = speed * 6
#     distance_10_hours = speed * 10
#     distance_15_hours = speed * 15
#
#     # 显示结果
#     print(f"The distance the car will travel in 6 hours is: {distance_6_hours} miles")
#     print(f"The distance the car will travel in 10 hours is: {distance_10_hours} miles")
#     print(f"The distance the car will travel in 15 hours is: {distance_15_hours} miles")
#
#
# # 调用函数
# if __name__ == "__main__":
#     distance_traveled()

# # Q6:
#
# def sales_tax_calculation():
#     # 定义州税和县税税率
#     state_tax_rate = 0.05
#     county_tax_rate = 0.025
#
#     # 询问用户输入购买金额
#     purchase_amount = float(input("Enter the amount of the purchase: $"))
#
#     # 计算州税和县税
#     state_tax = purchase_amount * state_tax_rate
#     county_tax = purchase_amount * county_tax_rate
#     total_tax = state_tax + county_tax
#
#     # 计算购买总金额（包括税）
#     total_sale = purchase_amount + total_tax
#
#     # 显示结果
#     print(f"Purchase Amount: ${purchase_amount:.2f}")
#     print(f"State Tax: ${state_tax:.2f}")
#     print(f"County Tax: ${county_tax:.2f}")
#     print(f"Total Tax: ${total_tax:.2f}")
#     print(f"Total Sale: ${total_sale:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     sales_tax_calculation()


# # q7:
#
# def calculate_mpg():
#     # 询问用户输入驾驶的里程数和使用的油量（加仑）
#     miles_driven = float(input("Enter the number of miles driven: "))
#     gallons_used = float(input("Enter the gallons of gas used: "))
#
#     # 计算每加仑行驶的里程数 (MPG)
#     mpg = miles_driven / gallons_used
#
#     # 显示结果
#     print(f"The car's MPG (Miles Per Gallon) is: {mpg:.2f} miles per gallon")
#
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_mpg()


# # Q8:
#
# def calculate_total_meal_cost():
#     # 定义小费率和税率
#     tip_rate = 0.18
#     sales_tax_rate = 0.07
#
#     # 询问用户输入餐费金额
#     meal_charge = float(input("Enter the charge for the meal: $"))
#
#     # 计算小费和销售税
#     tip = meal_charge * tip_rate
#     sales_tax = meal_charge * sales_tax_rate
#
#     # 计算总金额
#     total = meal_charge + tip + sales_tax
#
#     # 显示结果
#     print(f"Meal Charge: ${meal_charge:.2f}")
#     print(f"Tip: ${tip:.2f}")
#     print(f"Sales Tax: ${sales_tax:.2f}")
#     print(f"Total Amount: ${total:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_total_meal_cost()


# # Q9:
#
# def celsius_to_fahrenheit():
#     # 询问用户输入摄氏温度
#     celsius = float(input("Enter the temperature in Celsius: "))
#
#     # 将摄氏温度转换为华氏温度
#     fahrenheit = (9 / 5) * celsius + 32
#
#     # 显示结果
#     print(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     celsius_to_fahrenheit()


# # Q10:
#
# def ingredient_adjuster():
#     # 原始配方的配料量和饼干数量
#     sugar_per_48 = 1.5
#     butter_per_48 = 1
#     flour_per_48 = 2.75
#     cookies_per_recipe = 48
#
#     # 询问用户希望制作的饼干数量
#     desired_cookies = int(input("Enter the number of cookies you want to make: "))
#
#     # 计算调整后的配料量
#     sugar_needed = (sugar_per_48 / cookies_per_recipe) * desired_cookies
#     butter_needed = (butter_per_48 / cookies_per_recipe) * desired_cookies
#     flour_needed = (flour_per_48 / cookies_per_recipe) * desired_cookies
#
#     # 显示结果
#     print(f"To make {desired_cookies} cookies, you will need:")
#     print(f"{sugar_needed:.2f} cups of sugar")
#     print(f"{butter_needed:.2f} cups of butter")
#     print(f"{flour_needed:.2f} cups of flour")
#
#
# # 调用函数
# if __name__ == "__main__":
#     ingredient_adjuster()


# # Q11:
#
# def gender_percentage():
#     # 询问用户输入男性和女性的数量
#     num_males = int(input("Enter the number of males in the class: "))
#     num_females = int(input("Enter the number of females in the class: "))
#
#     # 计算总人数
#     total_students = num_males + num_females
#
#     # 计算男性和女性的百分比
#     percent_males = (num_males / total_students) * 100
#     percent_females = (num_females / total_students) * 100
#
#     # 显示结果
#     print(f"Percentage of males: {percent_males:.2f}%")
#     print(f"Percentage of females: {percent_females:.2f}%")
#
#
# # 调用函数
# if __name__ == "__main__":
#     gender_percentage()


# # Q12:
#
# def stock_transaction():
#     # 定义常量
#     shares = 2000
#     purchase_price_per_share = 40.00
#     sell_price_per_share = 42.75
#     commission_rate = 0.03
#
#     # 计算购买股票的总成本
#     amount_paid_for_stock = shares * purchase_price_per_share
#     purchase_commission = amount_paid_for_stock * commission_rate
#
#     # 计算出售股票的总收入
#     amount_received_from_sale = shares * sell_price_per_share
#     sale_commission = amount_received_from_sale * commission_rate
#
#     # 计算最终剩余金额（净利润或净亏损）
#     total_profit = (amount_received_from_sale - sale_commission) - (amount_paid_for_stock + purchase_commission)
#
#     # 显示结果
#     print(f"Amount paid for the stock: ${amount_paid_for_stock:.2f}")
#     print(f"Commission paid on the purchase: ${purchase_commission:.2f}")
#     print(f"Amount received from the sale: ${amount_received_from_sale:.2f}")
#     print(f"Commission paid on the sale: ${sale_commission:.2f}")
#     print(f"Net profit/loss: ${total_profit:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     stock_transaction()



# # Q13:

# def calculate_grapevines():
#     # 询问用户输入行的长度、端空间和葡萄藤之间的间距
#     row_length = float(input("Enter the length of the row (in feet): "))
#     end_space = float(input("Enter the space used by an end-post assembly (in feet): "))
#     space_between_vines = float(input("Enter the space between each vine (in feet): "))
#
#     # 计算可以种植的葡萄藤数量
#     num_vines = (row_length - 2 * end_space) / space_between_vines
#
#     # 显示结果
#     print(f"The number of grapevines that will fit in the row is: {int(num_vines)}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_grapevines()


# # Q14:
# def compound_interest():
#     # 询问用户输入本金、年利率、每年复利次数和存入年限
#     principal = float(input("Enter the principal amount: $"))
#     annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
#     times_compounded = int(input("Enter the number of times interest is compounded per year: "))
#     years = float(input("Enter the number of years the money will be left to grow: "))
#
#     # 计算复利后的总金额
#     amount = principal * (1 + annual_rate / times_compounded) ** (times_compounded * years)
#
#     # 显示结果
#     print(f"The amount of money in the account after {years} years is: ${amount:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     compound_interest()


# # # Q15:
# import turtle
# import tkinter as tk
# from tkinter import messagebox
#
# def create_turtle():
#     pen = turtle.Turtle()
#     pen.pensize(2)
#     pen.speed(3)
#     return pen
#
# def draw_square():
#     pen = create_turtle()
#     for _ in range(4):
#         pen.forward(100)
#         pen.right(90)
#     turtle.done()
#
# def draw_circle():
#     pen = create_turtle()
#     pen.circle(100)
#     turtle.done()
#
# def draw_triangle():
#     pen = create_turtle()
#     for _ in range(3):
#         pen.forward(100)
#         pen.right(120)
#     turtle.done()
#
# def draw_star():
#     pen = create_turtle()
#     for _ in range(5):
#         pen.forward(100)
#         pen.right(144)
#     turtle.done()
#
# def draw_hexagon():
#     pen = create_turtle()
#     for _ in range(6):
#         pen.forward(100)
#         pen.right(60)
#     turtle.done()
#
# def draw_spiral():
#     pen = create_turtle()
#     for i in range(50):
#         pen.forward(i * 5)
#         pen.right(45)
#     turtle.done()
#
# def start_drawing(choice):
#     turtle.clearscreen()  # 清除上一次绘制的图形
#     if choice == "Square":
#         draw_square()
#     elif choice == "Circle":
#         draw_circle()
#     elif choice == "Triangle":
#         draw_triangle()
#     elif choice == "Star":
#         draw_star()
#     elif choice == "Hexagon":
#         draw_hexagon()
#     elif choice == "Spiral":
#         draw_spiral()
#     else:
#         messagebox.showerror("Error", "Invalid choice.")
#
# def create_gui():
#     window = tk.Tk()
#     window.title("Turtle Graphics Drawing")
#
#     # 创建标签
#     label = tk.Label(window, text="Select a shape to draw:")
#     label.pack(pady=10)
#
#     # 创建选择框
#     shapes = ["Square", "Circle", "Triangle", "Star", "Hexagon", "Spiral"]
#     var = tk.StringVar(window)
#     var.set(shapes[0])  # 默认选择第一个形状
#
#     dropdown = tk.OptionMenu(window, var, *shapes)
#     dropdown.pack(pady=10)
#
#     # 创建绘制按钮
#     draw_button = tk.Button(
#         window,
#         text="Draw",
#         command=lambda: start_drawing(var.get())
#     )
#     draw_button.pack(pady=10)
#
#     # 创建退出按钮
#     quit_button = tk.Button(window, text="Quit", command=window.quit)
#     quit_button.pack(pady=10)
#
#     window.mainloop()
#
# # 调用函数启动GUI
# if __name__ == "__main__":
#     create_gui()


