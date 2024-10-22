# # Q1
# def kilometer_converter():
#     kilometers = float(input("Enter the distance in kilometers: "))
#     miles = kilometers * 0.6214
#     print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
#
# # 调用函数
# if __name__ == "__main__":
#     kilometer_converter()
#
#
# # Q2
# def calculate_county_tax(purchase_amount):
#     return purchase_amount * 0.025
#
# def calculate_state_tax(purchase_amount):
#     return purchase_amount * 0.05
#
# def display_total_tax(purchase_amount):
#     county_tax = calculate_county_tax(purchase_amount)
#     state_tax = calculate_state_tax(purchase_amount)
#     total_tax = county_tax + state_tax
#     total_amount = purchase_amount + total_tax
#
#     print(f"Purchase Amount: ${purchase_amount:.2f}")
#     print(f"County Tax: ${county_tax:.2f}")
#     print(f"State Tax: ${state_tax:.2f}")
#     print(f"Total Tax: ${total_tax:.2f}")
#     print(f"Total Amount: ${total_amount:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     purchase_amount = float(input("Enter the purchase amount: $"))
#     display_total_tax(purchase_amount)
#
#
# # Q3
# def calculate_insurance(replacement_cost):
#     return replacement_cost * 0.8
#
# def display_insurance():
#     replacement_cost = float(input("Enter the replacement cost of the building: $"))
#     insurance_needed = calculate_insurance(replacement_cost)
#     print(f"The minimum insurance amount you should buy is: ${insurance_needed:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_insurance()
#
#
# # Q4
# def calculate_automobile_costs():
#     loan_payment = float(input("Enter the monthly loan payment: $"))
#     insurance = float(input("Enter the monthly insurance cost: $"))
#     gas = float(input("Enter the monthly gas cost: $"))
#     oil = float(input("Enter the monthly oil cost: $"))
#     tires = float(input("Enter the monthly tires cost: $"))
#     maintenance = float(input("Enter the monthly maintenance cost: $"))
#
#     total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
#     total_annual_cost = total_monthly_cost * 12
#
#     print(f"Total monthly cost: ${total_monthly_cost:.2f}")
#     print(f"Total annual cost: ${total_annual_cost:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_automobile_costs()
#
#
# # Q5
# def calculate_assessment_value(actual_value):
#     return actual_value * 0.6
#
# def calculate_property_tax(assessment_value):
#     return (assessment_value / 100) * 0.72
#
# def display_property_tax():
#     actual_value = float(input("Enter the actual value of the property: $"))
#     assessment_value = calculate_assessment_value(actual_value)
#     property_tax = calculate_property_tax(assessment_value)
#
#     print(f"Assessment value: ${assessment_value:.2f}")
#     print(f"Property tax: ${property_tax:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_property_tax()
#
#
# # Q6
# def calculate_bmi(weight, height):
#     return weight / (height ** 2)
#
# def display_bmi():
#     weight = float(input("Enter your weight in kilograms: "))
#     height = float(input("Enter your height in meters: "))
#     bmi = calculate_bmi(weight, height)
#
#     print(f"Your BMI is: {bmi:.2f}")
#     if bmi < 18.5:
#         print("You are underweight.")
#     elif 18.5 <= bmi <= 24.9:
#         print("You have a normal weight.")
#     elif 25 <= bmi <= 29.9:
#         print("You are overweight.")
#     else:
#         print("You are obese.")
#
# # 调用函数
# if __name__ == "__main__":
#     display_bmi()
#
#
#
# # Q7
# def calories_burned_per_minute():
#     duration = int(input("Enter the duration of exercise in minutes: "))
#     calories_per_minute = float(input("Enter the calories burned per minute: "))
#     total_calories = duration * calories_per_minute
#     print(f"Total calories burned: {total_calories:.2f} calories")
#
# # 调用函数
# if __name__ == "__main__":
#     calories_burned_per_minute()
#
#
#
# # Q8
# def calculate_monthly_payment(principal, annual_rate, years):
#     monthly_rate = annual_rate / 12 / 100
#     months = years * 12
#     payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
#     return payment
#
# def display_monthly_payment():
#     principal = float(input("Enter the loan amount: $"))
#     annual_rate = float(input("Enter the annual interest rate (in %): "))
#     years = int(input("Enter the term of the loan in years: "))
#
#     monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
#     print(f"The monthly payment is: ${monthly_payment:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_monthly_payment()
#
#
# # Q9
# def calculate_tip(meal_cost):
#     return meal_cost * 0.15
#
# def calculate_tax(meal_cost):
#     return meal_cost * 0.07
#
# def display_tip_tax_total():
#     meal_cost = float(input("Enter the meal cost: $"))
#     tip = calculate_tip(meal_cost)
#     tax = calculate_tax(meal_cost)
#     total = meal_cost + tip + tax
#
#     print(f"Meal cost: ${meal_cost:.2f}")
#     print(f"Tip: ${tip:.2f}")
#     print(f"Tax: ${tax:.2f}")
#     print(f"Total: ${total:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_tip_tax_total()
#
#
#
# # Q10
# def calculate_compound_interest(principal, rate, times, years):
#     amount = principal * (1 + rate / times) ** (times * years)
#     return amount
#
# def display_compound_interest():
#     principal = float(input("Enter the initial investment amount: $"))
#     rate = float(input("Enter the annual interest rate (as a decimal): "))
#     times = int(input("Enter the number of times interest is compounded per year: "))
#     years = int(input("Enter the number of years: "))
#
#     future_value = calculate_compound_interest(principal, rate, times, years)
#     print(f"The investment value after {years} years is: ${future_value:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_compound_interest()
#
#
#
# # Q11
# def falling_distance(time):
#     gravity = 9.8  # m/s^2
#     distance = 0.5 * gravity * (time ** 2)
#     return distance
#
# def display_falling_distance():
#     for seconds in range(1, 11):
#         distance = falling_distance(seconds)
#         print(f"Time: {seconds} seconds - Distance: {distance:.2f} meters")
#
# # 调用函数
# if __name__ == "__main__":
#     display_falling_distance()
#
#
#
# # Q12
# def calculate_kinetic_energy(mass, velocity):
#     return 0.5 * mass * (velocity ** 2)
#
# def display_kinetic_energy():
#     mass = float(input("Enter the mass of the object (in kg): "))
#     velocity = float(input("Enter the velocity of the object (in m/s): "))
#     kinetic_energy = calculate_kinetic_energy(mass, velocity)
#     print(f"The kinetic energy of the object is: {kinetic_energy:.2f} joules")
#
# # 调用函数
# if __name__ == "__main__":
#     display_kinetic_energy()
#
#
# # Q13
# def determine_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     elif score >= 60:
#         return 'D'
#     else:
#         return 'F'
#
#
# def calculate_average(scores):
#     return sum(scores) / len(scores)
#
#
# def display_test_average_and_grade():
#     scores = []
#     for i in range(5):
#         score = float(input(f"Enter test score {i + 1}: "))
#         scores.append(score)
#         print(f"Score {i + 1}: {score} - Grade: {determine_grade(score)}")
#
#     average_score = calculate_average(scores)
#     print(f"\nAverage score: {average_score:.2f} - Grade: {determine_grade(average_score)}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     display_test_average_and_grade()
#
#
#
# # Q14
# def calculate_future_value(principal, rate, years):
#     future_value = principal * ((1 + rate) ** years)
#     return future_value
#
# def display_future_value():
#     principal = float(input("Enter the initial investment amount: $"))
#     rate = float(input("Enter the annual interest rate (as a decimal): "))
#     years = int(input("Enter the number of years: "))
#
#     future_value = calculate_future_value(principal, rate, years)
#     print(f"The future value of the investment is: ${future_value:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_future_value()
#
#
#
# # Q15
# import random
#
# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])
#
# def determine_winner(player, computer):
#     if player == computer:
#         return "It's a tie!"
#     elif (player == 'rock' and computer == 'scissors') or \
#          (player == 'scissors' and computer == 'paper') or \
#          (player == 'paper' and computer == 'rock'):
#         return "You win!"
#     else:
#         return "Computer wins!"
#
# def play_rock_paper_scissors():
#     player_choice = input("Enter rock, paper, or scissors: ").lower()
#     computer_choice = get_computer_choice()
#     print(f"Computer chose: {computer_choice}")
#     result = determine_winner(player_choice, computer_choice)
#     print(result)
#
# # 调用函数
# if __name__ == "__main__":
#     play_rock_paper_scissors()
#
#
#
# # Q16
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def check_prime():
#     number = int(input("Enter a number to check if it's prime: "))
#     if is_prime(number):
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")
#
# # 调用函数
# if __name__ == "__main__":
#     check_prime()
#
#
#
# # Q17
# import random
#
# def guessing_game():
#     number_to_guess = random.randint(1, 100)
#     guess = 0
#     attempts = 0
#
#     print("Guess the number between 1 and 100.")
#
#     while guess != number_to_guess:
#         guess = int(input("Enter your guess: "))
#         attempts += 1
#
#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You guessed it in {attempts} attempts.")
#
# # 调用函数
# if __name__ == "__main__":
#     guessing_game()
#
#
#
# # Q18
# def display_temperature_table():
#     print("Celsius\tFahrenheit")
#     print("-------------------")
#     for celsius in range(0, 21):
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius}\t{fahrenheit:.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     display_temperature_table()
#
#
#
# # Q19
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# def calculate_factorial():
#     number = int(input("Enter a non-negative integer: "))
#     if number < 0:
#         print("Error: The number must be non-negative.")
#     else:
#         result = factorial(number)
#         print(f"The factorial of {number} is: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_factorial()
#
#
#
# # Q20
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
# def calculate_gcd():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = gcd(num1, num2)
#     print(f"The GCD of {num1} and {num2} is: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_gcd()
#
#
#
# # Q21
# def recursive_sum(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + recursive_sum(n - 1)
#
# def calculate_recursive_sum():
#     number = int(input("Enter a positive integer: "))
#     if number < 0:
#         print("Error: The number must be positive.")
#     else:
#         result = recursive_sum(number)
#         print(f"The sum of numbers from 1 to {number} is: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_recursive_sum()
#
#
#
# # Q22
# def recursive_list_sum(num_list):
#     if len(num_list) == 0:
#         return 0
#     else:
#         return num_list[0] + recursive_list_sum(num_list[1:])
#
# def calculate_list_sum():
#     num_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#     result = recursive_list_sum(num_list)
#     print(f"The sum of the list is: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_list_sum()
#
#
#
# # Q23
# def recursive_power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * recursive_power(base, exponent - 1)
#
# def calculate_power():
#     base = float(input("Enter the base: "))
#     exponent = int(input("Enter the exponent: "))
#     result = recursive_power(base, exponent)
#     print(f"{base} raised to the power of {exponent} is: {result}")
#
# # 调用函数
# if __name__ == "__main__":
#     calculate_power()
#
#
#
#
#
#
#
