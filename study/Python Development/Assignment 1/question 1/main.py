# Question 1: Assume hot dogs come in packages of 10, and hotdog buns come in packages of 8. Write a program that
# calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with
# minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the
# number of hot dogs each person will be given. The program should display the following details:
# • The minimum number of packages of hot dogs required.
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over (10 Points)

import math

number_of_people = int(input("Enter the number of people: "))
hotdog_per_person = int(input("Enter the number of hotdogs per person: "))
total_of_hotdogs = number_of_people * hotdog_per_person

hotdog_leftover = total_of_hotdogs % 10
hotdogbun_leftover = total_of_hotdogs % 8
packages_of_hotdog = math.ceil(total_of_hotdogs / 10)
packages_of_hotdogbun = math.ceil(total_of_hotdogs / 8)

print(f"The minimum number of packages of hot dogs required: {packages_of_hotdog}")
print(f"The minimum number of packages of hot dog buns required: {packages_of_hotdogbun}")
print(f"The number of hot dogs left over: {hotdog_leftover}")
print(f"The number of hot dog buns left over: {hotdogbun_leftover}")
