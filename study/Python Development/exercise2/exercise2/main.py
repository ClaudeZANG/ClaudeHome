# # # Q1:
# # def day_of_the_week():
# #     # 询问用户输入一个数字
# #     day_number = int(input("Enter a number between 1 and 7: "))
# #
# #     # 映射数字到星期几
# #     days = {
# #         1: "Monday",
# #         2: "Tuesday",
# #         3: "Wednesday",
# #         4: "Thursday",
# #         5: "Friday",
# #         6: "Saturday",
# #         7: "Sunday"
# #     }
# #
# #     # 显示结果或错误信息
# #     if 1 <= day_number <= 7:
# #         print(f"The day is: {days[day_number]}")
# #     else:
# #         print("Error: The number must be between 1 and 7.")
# #
# # # 调用函数
# # if __name__ == "__main__":
# #     day_of_the_week()
#
#
# # Q2:
# def areas_of_rectangles():
#     # 输入第一个矩形的长度和宽度
#     length1 = float(input("Enter the length of the first rectangle: "))
#     width1 = float(input("Enter the width of the first rectangle: "))
#
#     # 输入第二个矩形的长度和宽度
#     length2 = float(input("Enter the length of the second rectangle: "))
#     width2 = float(input("Enter the width of the second rectangle: "))
#
#     # 计算面积
#     area1 = length1 * width1
#     area2 = length2 * width2
#
#     # 比较并输出结果
#     if area1 > area2:
#         print("The first rectangle has a larger area.")
#     elif area2 > area1:
#         print("The second rectangle has a larger area.")
#     else:
#         print("Both rectangles have the same area.")
#
# # 调用函数
# if __name__ == "__main__":
#     areas_of_rectangles()
#
#
# # Q3:
# def age_classifier():
#     # 输入年龄
#     age = int(input("Enter the age: "))
#
#     # 判断年龄分类
#     if age <= 1:
#         print("The person is an infant.")
#     elif 2 <= age <= 12:
#         print("The person is a child.")
#     elif 13 <= age <= 19:
#         print("The person is a teenager.")
#     else:
#         print("The person is an adult.")
#
# # 调用函数
# if __name__ == "__main__":
#     age_classifier()
#
#
# # Q4:
# def roman_numerals():
#     # 询问用户输入一个数字
#     number = int(input("Enter a number between 1 and 10: "))
#
#     # 映射数字到罗马数字
#     roman_numerals_map = {
#         1: "I",
#         2: "II",
#         3: "III",
#         4: "IV",
#         5: "V",
#         6: "VI",
#         7: "VII",
#         8: "VIII",
#         9: "IX",
#         10: "X"
#     }
#
#     # 显示结果或错误信息
#     if 1 <= number <= 10:
#         print(f"The Roman numeral for {number} is: {roman_numerals_map[number]}")
#     else:
#         print("Error: The number must be between 1 and 10.")
#
# # 调用函数
# if __name__ == "__main__":
#     roman_numerals()
#
#
# # Q5:
# def mass_and_weight():
#     # 询问用户输入物体质量（千克）
#     mass = float(input("Enter the mass of the object (in kilograms): "))
#
#     # 计算重量（牛顿）
#     weight = mass * 9.8
#
#     # 判断并显示结果
#     if weight > 500:
#         print(f"The object is too heavy. Its weight is {weight:.2f} Newtons.")
#     elif weight < 100:
#         print(f"The object is too light. Its weight is {weight:.2f} Newtons.")
#     else:
#         print(f"The object's weight is {weight:.2f} Newtons.")
#
# # 调用函数
# if __name__ == "__main__":
#     mass_and_weight()
#
#
# # Q6:
# def magic_dates():
#     # 询问用户输入月、日和年份
#     month = int(input("Enter the month (1-12): "))
#     day = int(input("Enter the day (1-31): "))
#     year = int(input("Enter the two-digit year (e.g., 21 for 2021): "))
#
#     # 判断是否是魔法日期
#     if month * day == year:
#         print(f"{month}/{day}/{year} is a magic date.")
#     else:
#         print(f"{month}/{day}/{year} is not a magic date.")
#
# # 调用函数
# if __name__ == "__main__":
#     magic_dates()
#
#
# # Q7:
# def color_mixer():
#     # 询问用户输入两个颜色
#     color1 = input("Enter the first primary color (red, blue, or yellow): ").lower()
#     color2 = input("Enter the second primary color (red, blue, or yellow): ").lower()
#
#     # 混合颜色的逻辑
#     if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
#         print("The mixed color is purple.")
#     elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
#         print("The mixed color is orange.")
#     elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
#         print("The mixed color is green.")
#     elif color1 == color2 and color1 in {"red", "blue", "yellow"}:
#         print(f"The colors are the same, so the result is still {color1}.")
#     else:
#         print("Error: Invalid primary colors. Please enter red, blue, or yellow.")
#
# # 调用函数
# if __name__ == "__main__":
#     color_mixer()
#
#
# # Q8:
# def hot_dog_cookout_calculator():
#     # 询问用户输入参与者人数和每人吃的热狗数量
#     num_people = int(input("Enter the number of people attending: "))
#     hot_dogs_per_person = int(input("Enter the number of hot dogs per person: "))
#
#     # 每包热狗和面包的数量
#     hot_dogs_per_package = 10
#     buns_per_package = 8
#
#     # 计算所需热狗总数和面包总数
#     total_hot_dogs = num_people * hot_dogs_per_person
#
#     # 计算所需热狗包数和面包包数，以及剩余数量
#     hot_dog_packages_needed = total_hot_dogs // hot_dogs_per_package
#     hot_dog_packages_leftover = total_hot_dogs % hot_dogs_per_package
#
#     bun_packages_needed = total_hot_dogs // buns_per_package
#     bun_packages_leftover = total_hot_dogs % buns_per_package
#
#     if hot_dog_packages_leftover > 0:
#         hot_dog_packages_needed += 1
#     if bun_packages_leftover > 0:
#         bun_packages_needed += 1
#
#     # 显示结果
#     print(f"You will need {hot_dog_packages_needed} packages of hot dogs and {bun_packages_needed} packages of buns.")
#     print(f"There will be {hot_dog_packages_leftover} leftover hot dogs and {bun_packages_leftover} leftover buns.")
#
# # 调用函数
# if __name__ == "__main__":
#     hot_dog_cookout_calculator()
#
#
# # Q9:
# def roulette_wheel():
#     pocket_number = int(input("Enter a pocket number (0-36): "))
#
#     if pocket_number == 0:
#         print("The pocket is green.")
#     elif 1 <= pocket_number <= 10:
#         color = "red" if pocket_number % 2 != 0 else "black"
#     elif 11 <= pocket_number <= 18:
#         color = "black" if pocket_number % 2 != 0 else "red"
#     elif 19 <= pocket_number <= 28:
#         color = "red" if pocket_number % 2 != 0 else "black"
#     elif 29 <= pocket_number <= 36:
#         color = "black" if pocket_number % 2 != 0 else "red"
#     else:
#         print("Error: Invalid pocket number.")
#         return
#
#     print(f"The pocket is {color}.")
#
# if __name__ == "__main__":
#     roulette_wheel()
#
#
# # Q10:
# def money_counting_game():
#     pennies = int(input("Enter the number of pennies: "))
#     nickels = int(input("Enter the number of nickels: "))
#     dimes = int(input("Enter the number of dimes: "))
#     quarters = int(input("Enter the number of quarters: "))
#
#     total_value = pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25
#
#     if total_value == 1.00:
#         print("Congratulations! The total is exactly one dollar.")
#     elif total_value < 1.00:
#         print(f"The total is less than one dollar. It is ${total_value:.2f}.")
#     else:
#         print(f"The total is more than one dollar. It is ${total_value:.2f}.")
#
# if __name__ == "__main__":
#     money_counting_game()
#
#
# # Q11:
# def book_club_points():
#     books_purchased = int(input("Enter the number of books purchased this month: "))
#
#     if books_purchased == 0:
#         points = 0
#     elif books_purchased == 1:
#         points = 5
#     elif books_purchased == 2:
#         points = 15
#     elif books_purchased == 3:
#         points = 30
#     elif books_purchased >= 4:
#         points = 60
#
#     print(f"You have earned {points} points.")
#
# if __name__ == "__main__":
#     book_club_points()
#
#
# # Q12:
# def software_sales():
#     quantity = int(input("Enter the number of packages purchased: "))
#     package_price = 99
#
#     if quantity < 10:
#         discount = 0
#     elif quantity < 20:
#         discount = 0.10
#     elif quantity < 50:
#         discount = 0.20
#     elif quantity < 100:
#         discount = 0.30
#     else:
#         discount = 0.40
#
#     discount_amount = quantity * package_price * discount
#     total = quantity * package_price - discount_amount
#
#     print(f"Discount amount: ${discount_amount:.2f}")
#     print(f"Total amount after discount: ${total:.2f}")
#
# if __name__ == "__main__":
#     software_sales()
#
#
# # Q13:
# def shipping_charges():
#     weight = float(input("Enter the weight of the package (in pounds): "))
#
#     if weight <= 2:
#         rate = 1.50
#     elif weight <= 6:
#         rate = 3.00
#     elif weight <= 10:
#         rate = 4.00
#     else:
#         rate = 4.75
#
#     shipping_cost = weight * rate
#
#     print(f"The shipping cost is: ${shipping_cost:.2f}")
#
# if __name__ == "__main__":
#     shipping_charges()
#
#
# # Q14:
# def body_mass_index():
#     weight = float(input("Enter your weight (in pounds): "))
#     height = float(input("Enter your height (in inches): "))
#
#     bmi = (weight / (height * height)) * 703
#
#     print(f"Your BMI is: {bmi:.2f}")
#     if bmi < 18.5:
#         print("You are underweight.")
#     elif 18.5 <= bmi <= 24.9:
#         print("You have a normal weight.")
#     else:
#         print("You are overweight.")
#
# if __name__ == "__main__":
#     body_mass_index()
#
#
# # Q15:
# def time_calculator():
#     total_seconds = int(input("Enter the number of seconds: "))
#
#     days = total_seconds // 86400
#     remaining_seconds = total_seconds % 86400
#     hours = remaining_seconds // 3600
#     remaining_seconds %= 3600
#     minutes = remaining_seconds // 60
#     seconds = remaining_seconds % 60
#
#     if total_seconds >= 86400:
#         print(f"{total_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
#     elif total_seconds >= 3600:
#         print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
#     elif total_seconds >= 60:
#         print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
#     else:
#         print(f"{total_seconds} seconds is less than a minute.")
#
# if __name__ == "__main__":
#     time_calculator()
#
#
# # Q16:
# def february_days():
#     year = int(input("Enter a year: "))
#
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"February in {year} has 29 days (leap year).")
#     else:
#         print(f"February in {year} has 28 days (common year).")
#
# if __name__ == "__main__":
#     february_days()
#
#
# # Q17:
# def wifi_diagnostic():
#     print("Reboot the computer and try to connect.")
#     response = input("Did that fix the problem? (yes/no): ").lower()
#
#     if response == "no":
#         print("Reboot the router and try to connect.")
#         response = input("Did that fix the problem? (yes/no): ").lower()
#
#         if response == "no":
#             print("Make sure the cables between the router and modem are plugged in firmly.")
#             response = input("Did that fix the problem? (yes/no): ").lower()
#
#             if response == "no":
#                 print("Move the router to a new location and try to connect.")
#                 response = input("Did that fix the problem? (yes/no): ").lower()
#
#                 if response == "no":
#                     print("Get a new router.")
#                 else:
#                     print("Problem solved.")
#             else:
#                 print("Problem solved.")
#         else:
#             print("Problem solved.")
#     else:
#         print("Problem solved.")
#
# if __name__ == "__main__":
#     wifi_diagnostic()
#
#
# # Q18:
# def restaurant_selector():
#     vegetarian = input("Is anyone in your party a vegetarian? (yes/no): ").lower()
#     vegan = input("Is anyone in your party a vegan? (yes/no): ").lower()
#     gluten_free = input("Is anyone in your party gluten-free? (yes/no): ").lower()
#
#     print("Here are your restaurant choices:")
#     if vegan == "yes":
#         print("Corner Café\nThe Chef's Kitchen")
#     elif vegetarian == "yes":
#         print("Main Street Pizza Company\nCorner Café\nMama's Fine Italian\nThe Chef's Kitchen")
#     elif gluten_free == "yes":
#         print("Main Street Pizza Company\nCorner Café\nThe Chef's Kitchen")
#     else:
#         print("Joe's Gourmet Burgers\nMain Street Pizza Company\nCorner Café\nMama's Fine Italian\nThe Chef's Kitchen")
#
# if __name__ == "__main__":
#     restaurant_selector()
#

# # Q19:
# import turtle
# import math
#
#
# def hit_the_target():
#     # 设置屏幕
#     screen = turtle.Screen()
#     screen.bgcolor("white")
#     screen.title("Hit the Target Game")
#
#     # 设置目标
#     target_x = 100
#     target_y = 100
#     target_radius = 25
#
#     # 绘制目标
#     target = turtle.Turtle()
#     target.penup()
#     target.goto(target_x, target_y - target_radius)
#     target.pendown()
#     target.circle(target_radius)
#     target.penup()
#     target.hideturtle()
#
#     # 设置射手
#     shooter = turtle.Turtle()
#     shooter.shape("triangle")
#     shooter.color("blue")
#     shooter.penup()
#     shooter.goto(-200, 0)
#     shooter.setheading(0)
#
#     # 输入角度和力道
#     angle = float(input("Enter the angle of the shot (0-90): "))
#     force = float(input("Enter the force of the shot (1-10): "))
#
#     # 设置射手角度
#     shooter.setheading(angle)
#     shooter.pendown()
#
#     # 移动射手
#     distance = force * 20
#     shooter.forward(distance)
#
#     # 检查命中
#     shot_x = shooter.xcor()
#     shot_y = shooter.ycor()
#     distance_to_target = math.sqrt((shot_x - target_x) ** 2 + (shot_y - target_y) ** 2)
#
#     if distance_to_target <= target_radius:
#         print("You hit the target!")
#     else:
#         print("You missed the target.")
#         if shot_x < target_x:
#             print("Try increasing the force or angle.")
#         elif shot_x > target_x:
#             print("Try decreasing the force or angle.")
#         if shot_y < target_y:
#             print("Try increasing the angle.")
#         elif shot_y > target_y:
#             print("Try decreasing the angle.")
#
#     # 结束绘图
#     turtle.done()
#
#
# if __name__ == "__main__":
#     hit_the_target()



