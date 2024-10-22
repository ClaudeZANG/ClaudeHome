# # Q1
# def bug_collector():
#     total_bugs = 0
#
#     # 循环5次，记录每天的虫子数量
#     for day in range(1, 6):
#         bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
#         total_bugs += bugs
#
#     print(f"The total number of bugs collected over 5 days is: {total_bugs}")
#
# # 调用函数
# if __name__ == "__main__":
#     bug_collector()
#
#
#
# # Q2
# def calories_burned():
#     calories_per_minute = 4.2
#
#     print("Calories burned on a treadmill:")
#     for minutes in [10, 15, 20, 25, 30]:
#         calories = calories_per_minute * minutes
#         print(f"After {minutes} minutes: {calories:.2f} calories burned")
#
# # 调用函数
# if __name__ == "__main__":
#     calories_burned()
#
#
#
# # Q3
# def budget_analysis():
#     budget = float(input("Enter your monthly budget: $"))
#     total_expenses = 0.0
#
#     while True:
#         expense = float(input("Enter an expense amount (enter 0 to stop): $"))
#         if expense == 0:
#             break
#         total_expenses += expense
#
#     if total_expenses > budget:
#         print(f"You are over budget by: ${total_expenses - budget:.2f}")
#     elif total_expenses < budget:
#         print(f"You are under budget by: ${budget - total_expenses:.2f}")
#     else:
#         print("You have exactly met your budget.")
#
# # 调用函数
# if __name__ == "__main__":
#     budget_analysis()
#
#
#
# # Q4
# def distance_traveled():
#     speed = float(input("Enter the speed of the vehicle (in mph): "))
#     time = int(input("Enter the time the vehicle has traveled (in hours): "))
#
#     print("Hour\tDistance Traveled")
#     print("-------------------------")
#     for hour in range(1, time + 1):
#         distance = speed * hour
#         print(f"{hour}\t\t{distance:.2f} miles")
#
# # 调用函数
# if __name__ == "__main__":
#     distance_traveled()
#
#
#
# # Q5
# def average_rainfall():
#     years = int(input("Enter the number of years: "))
#     total_rainfall = 0
#     months = 0
#
#     for year in range(1, years + 1):
#         for month in range(1, 13):
#             rainfall = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
#             total_rainfall += rainfall
#             months += 1
#
#     average_rainfall = total_rainfall / months
#     print(f"\nTotal months: {months}")
#     print(f"Total inches of rainfall: {total_rainfall:.2f}")
#     print(f"Average rainfall per month: {average_rainfall:.2f} inches")
#
# # 调用函数
# if __name__ == "__main__":
#     average_rainfall()
#
#
#
# # Q6
# def celsius_to_fahrenheit_table():
#     print("Celsius\tFahrenheit")
#     print("-----------------------")
#     for celsius in range(0, 21):
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius}\t\t{fahrenheit:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     celsius_to_fahrenheit_table()
#
#
#
# # Q7
# def pennies_for_pay():
#     days = int(input("Enter the number of days: "))
#     total_pay = 0.0
#     daily_pay = 0.01  # 初始工资为1美分
#
#     print("\nDay\tDaily Pay")
#     print("-------------------")
#     for day in range(1, days + 1):
#         print(f"{day}\t${daily_pay:.2f}")
#         total_pay += daily_pay
#         daily_pay *= 2  # 每天工资翻倍
#
#     print(f"\nTotal pay after {days} days is: ${total_pay:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     pennies_for_pay()
#
#
#
# # Q8
# def sum_of_numbers():
#     total = 0
#     while True:
#         number = float(input("Enter a positive number (negative to stop): "))
#         if number < 0:
#             break
#         total += number
#
#     print(f"The sum of the entered numbers is: {total}")
#
# # 调用函数
# if __name__ == "__main__":
#     sum_of_numbers()
#
#
#
# # Q9
# def ocean_levels():
#     rise_per_year = 1.6  # 每年上升1.6毫米
#
#     print("Year\tRise (mm)")
#     print("------------------")
#     for year in range(1, 26):
#         rise = rise_per_year * year
#         print(f"{year}\t{rise:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     ocean_levels()
#
#
#
# # Q10
# def tuition_increase():
#     tuition = 8000  # 假设初始学费为8000美元
#     increase_rate = 0.03  # 年增3%
#
#     print("Year\tTuition")
#     print("-------------------")
#     for year in range(1, 6):
#         tuition += tuition * increase_rate
#         print(f"{year}\t${tuition:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     tuition_increase()
#
#
#
# # Q11
# def weight_loss():
#     initial_weight = float(input("Enter your initial weight (in pounds): "))
#     weight_loss_per_week = 0.5  # 假设每周减0.5磅
#     weeks = 6 * 4  # 6个月 = 24周
#
#     print("Week\tWeight (pounds)")
#     print("---------------------------")
#     for week in range(1, weeks + 1):
#         weight = initial_weight - (weight_loss_per_week * week)
#         print(f"{week}\t{weight:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     weight_loss()
#
#
# # Q12
# def calculate_factorial():
#     number = int(input("Enter a non-negative integer: "))
#
#     if number < 0:
#         print("Error: The number must be non-negative.")
#         return
#
#     factorial = 1
#     for i in range(1, number + 1):
#         factorial *= i
#
#     print(f"The factorial of {number} is: {factorial}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_factorial()
#
#
#
# # Q13
# def population_growth():
#     initial_population = int(input("Enter the initial population: "))
#     daily_growth_rate = float(input("Enter the daily growth rate (as a percentage): ")) / 100
#     days = int(input("Enter the number of days: "))
#
#     print("Day\tPopulation")
#     print("---------------------")
#     for day in range(1, days + 1):
#         population = initial_population * ((1 + daily_growth_rate) ** day)
#         print(f"{day}\t{int(population)}")
#
# # 调用函数
# if __name__ == "__main__":
#     population_growth()
#
#
#
# # Q14
# def pattern_drawing_1():
#     rows = int(input("Enter the number of rows: "))
#
#     for i in range(rows, 0, -1):
#         print("*" * i)
#
# # 调用函数
# if __name__ == "__main__":
#     pattern_drawing_1()
#
#
#
# # Q15
# def pattern_drawing_2():
#     rows = int(input("Enter the number of rows: "))
#
#     for i in range(1, rows + 1):
#         print("#" * i)
#     for i in range(rows - 1, 0, -1):
#         print("#" * i)
#
# # 调用函数
# if __name__ == "__main__":
#     pattern_drawing_2()
#
#
#
# # Q16
# import turtle
#
# def draw_repeating_squares():
#     screen = turtle.Screen()
#     pen = turtle.Turtle()
#     pen.speed(0)  # 设置为最快速度
#
#     for i in range(36):
#         for _ in range(4):
#             pen.forward(100)
#             pen.right(90)
#         pen.right(10)  # 每次旋转10度
#
#     turtle.done()
#
# # 调用函数
# if __name__ == "__main__":
#     draw_repeating_squares()
#
#
#
# # Q17
# import turtle
#
# def draw_star_pattern():
#     screen = turtle.Screen()
#     pen = turtle.Turtle()
#     pen.speed(0)  # 设置为最快速度
#
#     for _ in range(5):
#         pen.forward(200)
#         pen.right(144)  # 星形的每个角度为144度
#
#     turtle.done()
#
# # 调用函数
# if __name__ == "__main__":
#     draw_star_pattern()
#
#
#
# # Q18
# import turtle
#
# def draw_hypnotic_pattern():
#     screen = turtle.Screen()
#     pen = turtle.Turtle()
#     pen.speed(0)  # 设置为最快速度
#     pen.color("blue")
#
#     for i in range(50):
#         pen.circle(100)
#         pen.left(10)  # 每次旋转10度
#
#     turtle.done()
#
# # 调用函数
# if __name__ == "__main__":
#     draw_hypnotic_pattern()
#
#
#
#
# # Q19
# import turtle
#
# def draw_stop_sign():
#     screen = turtle.Screen()
#     pen = turtle.Turtle()
#     pen.speed(3)  # 设置较慢速度，便于观察绘制过程
#
#     # 画八边形
#     pen.penup()
#     pen.goto(-100, 0)
#     pen.pendown()
#     pen.begin_fill()
#     pen.color("red")
#     for _ in range(8):
#         pen.forward(100)
#         pen.left(45)
#     pen.end_fill()
#
#     # 写入 "STOP"
#     pen.penup()
#     pen.goto(-60, -20)
#     pen.pendown()
#     pen.color("white")
#     pen.write("STOP", font=("Arial", 24, "bold"))
#
#     turtle.done()
#
# # 调用函数
# if __name__ == "__main__":
#     draw_stop_sign()
#

