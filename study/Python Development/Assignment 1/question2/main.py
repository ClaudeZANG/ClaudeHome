# Question 2: Write a program that asks the user to enter the monthly costs for the following expenses incurred from
# operating his or her automobile: loan payment, insurance, gas, and maintenance. The program should then display the
# total monthly costs for these expenses and the total annual costs for these expenses. (10 marks)

month_loan_payment = float(input("Enter the loan payment per month: "))
month_insurance = float(input("Enter the insurance per month: "))
month_gas = float(input("Enter the gas per month: "))
month_maintenance = float(input("Enter the maintenance per month: "))

annual_loan_payment = month_loan_payment * 12
annual_insurance = month_insurance * 12
annual_gas = month_gas * 12
annual_maintenance = month_maintenance * 12

total_monthly_cost = month_loan_payment + month_insurance + month_gas + month_maintenance
total_annual_cost = annual_loan_payment + annual_insurance + annual_gas + annual_maintenance

print(f"The total monthly cost is {total_monthly_cost}")
print(f"The total annual cost is {total_annual_cost}")
print(f"The total annual cost of loan payment is {annual_loan_payment}")
print(f"The total annual cost of insurance is {annual_insurance}")
print(f"The total annual cost of gas is {annual_gas}")
print(f"The total annual cost of maintenance is {annual_maintenance}")