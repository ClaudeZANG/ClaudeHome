# # Q1
# def total_sales():
#     sales = []
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     for day in days:
#         sale = float(input(f"Enter sales for {day}: $"))
#         sales.append(sale)
#
#     total = sum(sales)
#     print(f"Total sales for the week: ${total:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     total_sales()
#
#
#
# # Q2
# import random
#
# def lottery_number_generator():
#     lottery_numbers = [random.randint(0, 9) for _ in range(7)]
#     print("Generated lottery numbers:", lottery_numbers)
#
# # 调用函数
# if __name__ == "__main__":
#     lottery_number_generator()
#
#
# # Q3
# def rainfall_statistics():
#     months = ["January", "February", "March", "April", "May", "June",
#               "July", "August", "September", "October", "November", "December"]
#     rainfall = []
#
#     for month in months:
#         amount = float(input(f"Enter rainfall for {month}: "))
#         rainfall.append(amount)
#
#     total_rainfall = sum(rainfall)
#     average_rainfall = total_rainfall / len(rainfall)
#     max_rainfall = max(rainfall)
#     min_rainfall = min(rainfall)
#     max_month = months[rainfall.index(max_rainfall)]
#     min_month = months[rainfall.index(min_rainfall)]
#
#     print(f"Total rainfall for the year: {total_rainfall} inches")
#     print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
#     print(f"Highest rainfall in {max_month}: {max_rainfall} inches")
#     print(f"Lowest rainfall in {min_month}: {min_rainfall} inches")
#
#
# # 调用函数
# if __name__ == "__main__":
#     rainfall_statistics()
#
#
# # Q4
# def number_analysis_program():
#     numbers = []
#     for i in range(1, 21):
#         number = float(input(f"Enter number {i}: "))
#         numbers.append(number)
#
#     lowest = min(numbers)
#     highest = max(numbers)
#     total = sum(numbers)
#     average = total / len(numbers)
#
#     print(f"Lowest number: {lowest}")
#     print(f"Highest number: {highest}")
#     print(f"Total of the numbers: {total}")
#     print(f"Average of the numbers: {average:.2f}")
#
#
# # 调用函数
# if __name__ == "__main__":
#     number_analysis_program()
#
#
# # Q5
# def charge_account_validation():
#     try:
#         with open('charge_accounts.txt', 'r') as file:
#             valid_accounts = [line.strip() for line in file]
#
#         account_number = input("Enter a charge account number: ")
#
#         if account_number in valid_accounts:
#             print("The account number is valid.")
#         else:
#             print("The account number is invalid.")
#     except FileNotFoundError:
#         print("The file charge_accounts.txt does not exist.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     charge_account_validation()
#
#
# # Q6
# def larger_than_n(numbers, n):
#     print(f"Numbers greater than {n}:")
#     for num in numbers:
#         if num > n:
#             print(num)
#
# def get_input_and_find_larger():
#     numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
#     n = int(input("Enter the number n: "))
#     larger_than_n(numbers, n)
#
# # 调用函数
# if __name__ == "__main__":
#     get_input_and_find_larger()
#
#
# # Q7
# def drivers_license_exam():
#     correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
#                        'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#     student_answers = []
#
#     try:
#         with open('student_answers.txt', 'r') as file:
#             for line in file:
#                 student_answers.append(line.strip().upper())
#
#         correct_count = sum(1 for i in range(20) if student_answers[i] == correct_answers[i])
#         passed = correct_count >= 15
#
#         print(f"You answered {correct_count} questions correctly.")
#         print("You passed!" if passed else "You did not pass.")
#         incorrect_questions = [i + 1 for i in range(20) if student_answers[i] != correct_answers[i]]
#         print(f"Questions you got wrong: {incorrect_questions}")
#     except FileNotFoundError:
#         print("The file student_answers.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     drivers_license_exam()
#
#
# # Q8
# def name_search():
#     try:
#         with open('GirlNames.txt', 'r') as girl_file:
#             girl_names = {line.strip() for line in girl_file}
#
#         with open('BoyNames.txt', 'r') as boy_file:
#             boy_names = {line.strip() for line in boy_file}
#
#         name = input("Enter a name to search: ").capitalize()
#         is_girl_name = name in girl_names
#         is_boy_name = name in boy_names
#
#         if is_girl_name and is_boy_name:
#             print(f"{name} is a popular name for both girls and boys.")
#         elif is_girl_name:
#             print(f"{name} is a popular name for girls.")
#         elif is_boy_name:
#             print(f"{name} is a popular name for boys.")
#         else:
#             print(f"{name} is not a popular name.")
#     except FileNotFoundError:
#         print("One or both files (GirlNames.txt, BoyNames.txt) do not exist.")
#
#
# # 调用函数
# if __name__ == "__main__":
#     name_search()
#
#
# # Q9
# def population_data_analysis():
#     try:
#         with open('USPopulation.txt', 'r') as file:
#             population = [int(line.strip()) for line in file]
#
#         changes = [population[i] - population[i - 1] for i in range(1, len(population))]
#         average_change = sum(changes) / len(changes)
#         max_change = max(changes)
#         min_change = min(changes)
#         max_year = 1950 + changes.index(max_change) + 1
#         min_year = 1950 + changes.index(min_change) + 1
#
#         print(f"Average annual change: {average_change:.2f}")
#         print(f"Greatest increase in population: {max_change} in {max_year}")
#         print(f"Smallest increase in population: {min_change} in {min_year}")
#     except FileNotFoundError:
#         print("The file USPopulation.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     population_data_analysis()
#
#
# # Q10
# def world_series_champions():
#     try:
#         with open('WorldSeriesWinners.txt', 'r') as file:
#             winners = [line.strip() for line in file]
#
#         team = input("Enter the name of a team: ")
#         win_count = winners.count(team)
#
#         print(f"The {team} won the World Series {win_count} times.")
#     except FileNotFoundError:
#         print("The file WorldSeriesWinners.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     world_series_champions()
#
#
# # Q11
# def is_lo_shu_magic_square(square):
#     flattened = [num for row in square for num in row]
#     if sorted(flattened) != list(range(1, 10)):
#         return False
#
#     target_sum = sum(square[0])
#     for row in square:
#         if sum(row) != target_sum:
#             return False
#
#     for col in range(3):
#         if sum(square[row][col] for row in range(3)) != target_sum:
#             return False
#
#     if sum(square[i][i] for i in range(3)) != target_sum:
#         return False
#     if sum(square[i][2 - i] for i in range(3)) != target_sum:
#         return False
#
#     return True
#
# def test_magic_square():
#     square = [[int(input(f"Enter number for row {i+1}, column {j+1}: ")) for j in range(3)] for i in range(3)]
#     if is_lo_shu_magic_square(square):
#         print("This is a Lo Shu Magic Square.")
#     else:
#         print("This is not a Lo Shu Magic Square.")
#
# # 调用函数
# if __name__ == "__main__":
#     test_magic_square()
#
#
#
# # Q12
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def generate_primes():
#     upper_limit = int(input("Enter an integer greater than 1: "))
#     primes = [num for num in range(2, upper_limit + 1) if is_prime(num)]
#     print(f"Prime numbers up to {upper_limit}: {primes}")
#
# # 调用函数
# if __name__ == "__main__":
#     generate_primes()
#
#
#
# # Q13
# import random
#
# def magic_8_ball():
#     try:
#         with open('8_ball_responses.txt', 'r') as file:
#             responses = [line.strip() for line in file]
#
#         while True:
#             question = input("Ask a yes or no question (or type 'quit' to stop): ")
#             if question.lower() == 'quit':
#                 break
#             print("Magic 8 Ball says:", random.choice(responses))
#     except FileNotFoundError:
#         print("The file 8_ball_responses.txt does not exist.")
#
# # 调用函数
# if __name__ == "__main__":
#     magic_8_ball()
#
#
# # Q14
# import matplotlib.pyplot as plt
#
# def plot_expense_pie_chart():
#     try:
#         with open('expenses.txt', 'r') as file:
#             expenses = {}
#             for line in file:
#                 category, amount = line.strip().split(':')
#                 expenses[category] = float(amount)
#
#         categories = list(expenses.keys())
#         amounts = list(expenses.values())
#
#         plt.pie(amounts, labels=categories, autopct='%1.1f%%')
#         plt.title('Monthly Expenses')
#         plt.show()
#     except FileNotFoundError:
#         print("The file expenses.txt does not exist.")
#     except ValueError:
#         print("The file contains invalid data.")
#
# # 调用函数
# if __name__ == "__main__":
#     plot_expense_pie_chart()
#
#
# # Q15
# import matplotlib.pyplot as plt
#
# def plot_gas_prices():
#     try:
#         with open('1994_Weekly_Gas_Averages.txt', 'r') as file:
#             gas_prices = [float(line.strip()) for line in file]
#
#         weeks = list(range(1, len(gas_prices) + 1))
#
#         plt.plot(weeks, gas_prices, marker='o')
#         plt.title('1994 Weekly Gas Prices')
#         plt.xlabel('Week')
#         plt.ylabel('Average Price (USD)')
#         plt.grid(True)
#         plt.show()
#     except FileNotFoundError:
#         print("The file 1994_Weekly_Gas_Averages.txt does not exist.")
#     except ValueError:
#         print("The file contains invalid data.")
#
# # 调用函数
# if __name__ == "__main__":
#     plot_gas_prices()
