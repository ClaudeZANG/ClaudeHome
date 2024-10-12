# A painting company has determined that for every 112 square feet of wall space, one gallon of paint is required. The
# company charges $25.00 per hour for labour. Write a program that asks the user to enter the number of square feet of
# wall space to be painted and the price of the paint per gallon.
# The program should then display the following data.
# • The number of gallons of paint required
# • The cost of the paint
# • The hours of labour required to complete the job
# • The cost of the labour to complete the job
# • The total cost of the paint job.
# Assume that the program will run only once for each estimate. (10 marks)

import math

wall_space = float(input("Enter the sqft of wall space: "))
price_per_gallon = float(input("Enter the price of paint per gallon: "))
labour_sqft_hours = float(input("Enter the amount wall sqft the labour can paint per hour: "))
labour_hours = math.ceil(wall_space / labour_sqft_hours)

gallons_required = math.ceil(wall_space / 112)
paint_cost = gallons_required * price_per_gallon
cost_of_labour = labour_hours * 25.00
total_cost = paint_cost + cost_of_labour

print(f"The number of gallons of paint required is {gallons_required}")
print(f"The cost of the paint is {paint_cost:.2f}")
print(f"The hours of labour required to complete the job is {labour_hours}")
print(f"The cost of the labour to complete the job is {cost_of_labour:.2f}")
print(f"The total cost of the paint job is {total_cost:.2f}")