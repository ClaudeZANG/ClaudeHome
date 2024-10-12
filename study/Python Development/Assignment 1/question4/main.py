# Question 4: A Personal Fitness tracker is a wearable device that tracks one’s physical activity, calories burned,
# heart rate, sleeping patterns and so on. One common physical activity that is tracked is the number of steps that you
# take each day. The File named Steps.txt contains the number of steps that a user has made each day for an entire year
# (Jan 1 to Dec 31) Write a program that reads the file, then displays the average number of steps taken for each month.
# Assume the data is from a year that is not a leap year, therefore, February has 28 days. The program should then
# count the number of days in the year that the user has made 10,000 steps or more and display the number of days
# with 10000 or more steps. (10 marks)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('supplementary file.txt', 'r') as file:
    steps = [int(line.strip()) for line in file]

if len(steps) != 365:
    print("Error!")
else:
    start_day = 0
    for month, days in enumerate(days_in_month):
        month_steps = steps[start_day:start_day + days]
        average_steps = sum(month_steps) / days
        print(f"Month {month + 1} average steps: {average_steps:.2f}")
        start_day += days

    days_with_10000_steps = sum(1 for step in steps if step >= 10000)
    print(f"Number of days with 10,000 or more steps: {days_with_10000_steps}")
