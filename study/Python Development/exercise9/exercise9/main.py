# # Q1
# class Pet:
#     def __init__(self, name, animal_type, age):
#         self.__name = name
#         self.__animal_type = animal_type
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_animal_type(self, animal_type):
#         self.__animal_type = animal_type
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
# def main():
#     name = input("Enter the pet's name: ")
#     animal_type = input("Enter the type of animal: ")
#     age = int(input("Enter the pet's age: "))
#
#     pet = Pet(name, animal_type, age)
#
#     print("\nPet Information:")
#     print(f"Name: {pet.get_name()}")
#     print(f"Type: {pet.get_animal_type()}")
#     print(f"Age: {pet.get_age()}")
#
# # 调用函数
# if __name__ == "__main__":
#     main()
#
#
# # Q2
# class Car:
#     def __init__(self, year_model, make):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 5
#
#     def brake(self):
#         self.__speed -= 5
#
#     def get_speed(self):
#         return self.__speed
#
# def main():
#     car = Car(2023, 'Toyota')
#
#     for _ in range(5):
#         car.accelerate()
#         print(f"Accelerating: Current speed is {car.get_speed()} km/h")
#
#     for _ in range(5):
#         car.brake()
#         print(f"Braking: Current speed is {car.get_speed()} km/h")
#
# # 调用函数
# if __name__ == "__main__":
#     main()
#
#
# # Q3
# class PersonalInfo:
#     def __init__(self, name, address, age, phone):
#         self.__name = name
#         self.__address = address
#         self.__age = age
#         self.__phone = phone
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_address(self, address):
#         self.__address = address
#
#     def set_age(self, age):
#         self.__age = age
#
#     def set_phone(self, phone):
#         self.__phone = phone
#
#     def get_name(self):
#         return self.__name
#
#     def get_address(self):
#         return self.__address
#
#     def get_age(self):
#         return self.__age
#
#     def get_phone(self):
#         return self.__phone
#
# def main():
#     person1 = PersonalInfo("John Doe", "123 Main St", 30, "555-1234")
#     person2 = PersonalInfo("Jane Smith", "456 Elm St", 25, "555-5678")
#     person3 = PersonalInfo("Mike Brown", "789 Oak St", 40, "555-8765")
#
#     people = [person1, person2, person3]
#
#     for person in people:
#         print(f"\nName: {person.get_name()}")
#         print(f"Address: {person.get_address()}")
#         print(f"Age: {person.get_age()}")
#         print(f"Phone: {person.get_phone()}")
#
# # 调用函数
# if __name__ == "__main__":
#     main()
#
#
# # Q4
# class Employee:
#     def __init__(self, name, id_number, department, job_title):
#         self.__name = name
#         self.__id_number = id_number
#         self.__department = department
#         self.__job_title = job_title
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_id_number(self, id_number):
#         self.__id_number = id_number
#
#     def set_department(self, department):
#         self.__department = department
#
#     def set_job_title(self, job_title):
#         self.__job_title = job_title
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_number(self):
#         return self.__id_number
#
#     def get_department(self):
#         return self.__department
#
#     def get_job_title(self):
#         return self.__job_title
#
# def main():
#     emp1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
#     emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")
#     emp3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")
#
#     employees = [emp1, emp2, emp3]
#
#     for emp in employees:
#         print(f"\nName: {emp.get_name()}")
#         print(f"ID Number: {emp.get_id_number()}")
#         print(f"Department: {emp.get_department()}")
#         print(f"Job Title: {emp.get_job_title()}")
#
# # 调用函数
# if __name__ == "__main__":
#     main()
#
#
# # Q5
# class RetailItem:
#     def __init__(self, description, units, price):
#         self.__description = description
#         self.__units = units
#         self.__price = price
#
#     def get_description(self):
#         return self.__description
#
#     def get_units(self):
#         return self.__units
#
#     def get_price(self):
#         return self.__price
#
# def main():
#     item1 = RetailItem("Jacket", 12, 59.95)
#     item2 = RetailItem("Designer Jeans", 40, 34.95)
#     item3 = RetailItem("Shirt", 20, 24.95)
#
#     items = [item1, item2, item3]
#
#     for item in items:
#         print(f"\nDescription: {item.get_description()}")
#         print(f"Units in Inventory: {item.get_units()}")
#         print(f"Price: ${item.get_price():.2f}")
#
# # 调用函数
# if __name__ == "__main__":
#     main()
#
#
# # Q6
# class Patient:
#     def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name,
#                  emergency_phone):
#         self.__first_name = first_name
#         self.__middle_name = middle_name
#         self.__last_name = last_name
#         self.__address = address
#         self.__city = city
#         self.__state = state
#         self.__zip_code = zip_code
#         self.__phone = phone
#         self.__emergency_name = emergency_name
#         self.__emergency_phone = emergency_phone
#
#     # Accessor methods (omitted for brevity)
#     def get_full_name(self):
#         return f"{self.__first_name} {self.__middle_name} {self.__last_name}"
#
#
# class Procedure:
#     def __init__(self, procedure_name, date, practitioner, charge):
#         self.__procedure_name = procedure_name
#         self.__date = date
#         self.__practitioner = practitioner
#         self.__charge = charge
#
#     def get_charge(self):
#         return self.__charge
#
#     # Accessor methods (omitted for brevity)
#
#
# def main():
#     patient = Patient("John", "M.", "Doe", "123 Main St", "Anytown", "CA", "12345", "555-1234", "Jane Doe", "555-4321")
#     procedure1 = Procedure("Physical Exam", "2024-10-21", "Dr. Irvine", 250.00)
#     procedure2 = Procedure("X-ray", "2024-10-21", "Dr. Jamison", 500.00)
#     procedure3 = Procedure("Blood test", "2024-10-21", "Dr. Smith", 200.00)
#
#     total_charge = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()
#
#     print(f"Patient: {patient.get_full_name()}")
#     print(f"Total charges: ${total_charge:.2f}")
#
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q7
# import pickle
#
# class Employee:
#     def __init__(self, name, department, job_title):
#         self.__name = name
#         self.__department = department
#         self.__job_title = job_title
#
#     # Accessor methods (omitted for brevity)
#
# def main():
#     try:
#         with open('employees.pkl', 'rb') as file:
#             employees = pickle.load(file)
#     except (FileNotFoundError, EOFError):
#         employees = {}
#
#     while True:
#         print("\nMenu:")
#         print("1. Look up an employee")
#         print("2. Add a new employee")
#         print("3. Update an employee")
#         print("4. Delete an employee")
#         print("5. Quit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == '1':
#             emp_id = input("Enter the employee ID: ")
#             print(employees.get(emp_id, 'Employee not found'))
#
#         elif choice == '2':
#             emp_id = input("Enter the employee ID: ")
#             name = input("Enter the employee's name: ")
#             department = input("Enter the department: ")
#             job_title = input("Enter the job title: ")
#             employees[emp_id] = Employee(name, department, job_title)
#
#         elif choice == '3':
#             emp_id = input("Enter the employee ID: ")
#             if emp_id in employees:
#                 name = input("Enter the new name: ")
#                 department = input("Enter the new department: ")
#                 job_title = input("Enter the new job title: ")
#                 employees[emp_id] = Employee(name, department, job_title)
#             else:
#                 print("Employee not found")
#
#         elif choice == '4':
#             emp_id = input("Enter the employee ID to delete: ")
#             if emp_id in employees:
#                 del employees[emp_id]
#                 print("Employee deleted.")
#             else:
#                 print("Employee not found.")
#
#         elif choice == '5':
#             with open('employees.pkl', 'wb') as file:
#                 pickle.dump(employees, file)
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q8
# class RetailItem:
#     def __init__(self, description, units, price):
#         self.description = description
#         self.units = units
#         self.price = price
#
# class CashRegister:
#     def __init__(self):
#         self.items = []
#
#     def purchase_item(self, item):
#         self.items.append(item)
#
#     def get_total(self):
#         return sum(item.price for item in self.items)
#
#     def show_items(self):
#         for item in self.items:
#             print(f"{item.description}: ${item.price:.2f}")
#
#     def clear(self):
#         self.items = []
#
# def main():
#     item1 = RetailItem("Jacket", 12, 59.95)
#     item2 = RetailItem("Designer Jeans", 40, 34.95)
#     item3 = RetailItem("Shirt", 20, 24.95)
#
#     register = CashRegister()
#     register.purchase_item(item1)
#     register.purchase_item(item2)
#     register.purchase_item(item3)
#
#     print("Items in the cart:")
#     register.show_items()
#     print(f"Total price: ${register.get_total():.2f}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
# # Q9
# class Question:
#     def __init__(self, question, answer1, answer2, answer3, answer4, correct):
#         self.question = question
#         self.answers = [answer1, answer2, answer3, answer4]
#         self.correct = correct
#
#     def ask(self):
#         print(self.question)
#         for i, answer in enumerate(self.answers, start=1):
#             print(f"{i}. {answer}")
#         choice = int(input("Your answer (1-4): "))
#         return choice == self.correct
#
# def main():
#     questions = [
#         Question("What is the capital of France?", "Paris", "London", "Rome", "Berlin", 1),
#         Question("What is 2 + 2?", "3", "4", "5", "6", 2),
#         # Add more questions as needed
#     ]
#
#     player1_score = 0
#     player2_score = 0
#
#     print("Player 1's turn:")
#     for question in questions[:5]:
#         if question.ask():
#             player1_score += 1
#
#     print("\nPlayer 2's turn:")
#     for question in questions[5:]:
#         if question.ask():
#             player2_score += 1
#
#     print(f"\nPlayer 1's score: {player1_score}")
#     print(f"Player 2's score: {player2_score}")
#     if player1_score > player2_score:
#         print("Player 1 wins!")
#     elif player2_score > player1_score:
#         print("Player 2 wins!")
#     else:
#         print("It's a tie!")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
#
#
#
# # Q10
# class Employee:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def get_name(self):
#         return self.name
#
#     def get_number(self):
#         return self.number
#
# class ProductionWorker(Employee):
#     def __init__(self, name, number, shift, hourly_pay):
#         super().__init__(name, number)
#         self.shift = shift
#         self.hourly_pay = hourly_pay
#
#     def get_shift(self):
#         return "Day" if self.shift == 1 else "Night"
#
#     def get_hourly_pay(self):
#         return self.hourly_pay
#
# def main():
#     name = input("Enter the worker's name: ")
#     number = input("Enter the worker's number: ")
#     shift = int(input("Enter the shift (1 for day, 2 for night): "))
#     hourly_pay = float(input("Enter the hourly pay: "))
#
#     worker = ProductionWorker(name, number, shift, hourly_pay)
#
#     print("\nWorker Details:")
#     print(f"Name: {worker.get_name()}")
#     print(f"Number: {worker.get_number()}")
#     print(f"Shift: {worker.get_shift()}")
#     print(f"Hourly Pay: ${worker.get_hourly_pay():.2f}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
# # Q11
# class Employee:
#     def __init__(self, name, number):
#         self.__name = name
#         self.__number = number
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_number(self, number):
#         self.__number = number
#
#     def get_name(self):
#         return self.__name
#
#     def get_number(self):
#         return self.__number
#
# class ShiftSupervisor(Employee):
#     def __init__(self, name, number, salary, bonus):
#         super().__init__(name, number)
#         self.__salary = salary
#         self.__bonus = bonus
#
#     def set_salary(self, salary):
#         self.__salary = salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_salary(self):
#         return self.__salary
#
#     def get_bonus(self):
#         return self.__bonus
#
# def main():
#     name = input("Enter the shift supervisor's name: ")
#     number = input("Enter the shift supervisor's employee number: ")
#     salary = float(input("Enter the shift supervisor's annual salary: "))
#     bonus = float(input("Enter the shift supervisor's annual production bonus: "))
#
#     supervisor = ShiftSupervisor(name, number, salary, bonus)
#
#     print("\nShift Supervisor Details:")
#     print(f"Name: {supervisor.get_name()}")
#     print(f"Employee Number: {supervisor.get_number()}")
#     print(f"Annual Salary: ${supervisor.get_salary():,.2f}")
#     print(f"Annual Bonus: ${supervisor.get_bonus():,.2f}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
#
# # Q12
# class Person:
#     def __init__(self, name, address, phone):
#         self.__name = name
#         self.__address = address
#         self.__phone = phone
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_address(self, address):
#         self.__address = address
#
#     def set_phone(self, phone):
#         self.__phone = phone
#
#     def get_name(self):
#         return self.__name
#
#     def get_address(self):
#         return self.__address
#
#     def get_phone(self):
#         return self.__phone
#
# class Customer(Person):
#     def __init__(self, name, address, phone, customer_number, mailing_list):
#         super().__init__(name, address, phone)
#         self.__customer_number = customer_number
#         self.__mailing_list = mailing_list
#
#     def set_customer_number(self, customer_number):
#         self.__customer_number = customer_number
#
#     def set_mailing_list(self, mailing_list):
#         self.__mailing_list = mailing_list
#
#     def get_customer_number(self):
#         return self.__customer_number
#
#     def get_mailing_list(self):
#         return self.__mailing_list
#
# def main():
#     name = input("Enter the customer's name: ")
#     address = input("Enter the customer's address: ")
#     phone = input("Enter the customer's phone number: ")
#     customer_number = input("Enter the customer number: ")
#     mailing_list = input("Is the customer on the mailing list? (yes/no): ").lower() == 'yes'
#
#     customer = Customer(name, address, phone, customer_number, mailing_list)
#
#     print("\nCustomer Details:")
#     print(f"Name: {customer.get_name()}")
#     print(f"Address: {customer.get_address()}")
#     print(f"Phone Number: {customer.get_phone()}")
#     print(f"Customer Number: {customer.get_customer_number()}")
#     print(f"Mailing List: {'Yes' if customer.get_mailing_list() else 'No'}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()
#
