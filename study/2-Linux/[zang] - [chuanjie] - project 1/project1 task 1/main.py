# Define a dictionary to store monthly budget and expenses for users
budget_data = {}

# Function to add an expense
def add_expense(user, amount):
    if user in budget_data:
        budget_data[user] -= amount
    else:
        budget_data[user] = -amount

# Function to remove an expense
def remove_expense(user, amount):
    if user in budget_data:
        budget_data[user] += amount

# Function to add revenue
def add_revenue(user, amount):
    if user in budget_data:
        budget_data[user] += amount
    else:
        budget_data[user] = amount

# Function to remove revenue
def remove_revenue(user, amount):
    if user in budget_data:
        budget_data[user] -= amount

# Function to check budget balance
def check_budget_balance(user):
    if user in budget_data:
        return budget_data[user]
    else:
        return 0

# Function to get username
def get_username():
    user = input("Enter user name: ")
    return user

# Main function to run the program
def main():
    user = get_username()
    while True:
        # Print menu
        print("\nMenu Selections:")
        print("1. Add an Expense")
        print("2. Remove an Expense")
        print("3. Add Revenue")
        print("4. Remove Revenue")
        print("5. Check Budget Balance")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Perform operations based on user choice
        if choice == '1':
            amount = float(input("Enter expense amount: "))
            add_expense(user, amount)
            print("Expense added successfully!")
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            remove_expense(user, amount)
            print("Expense removed successfully!")
        elif choice == '3':
            amount = float(input("Enter revenue amount: "))
            add_revenue(user, amount)
            print("Revenue added successfully!")
        elif choice == '4':
            amount = float(input("Enter revenue amount: "))
            remove_revenue(user, amount)
            print("Revenue removed successfully!")
        elif choice == '5':
            balance = check_budget_balance(user)
            print(f"Current balance for {user}: {balance}")
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
