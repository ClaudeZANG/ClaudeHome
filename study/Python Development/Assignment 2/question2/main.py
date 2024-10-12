import matplotlib.pyplot as plt


def read_expenses(file_name):
    expenses = {}
    try:
        # open file and read
        with open(file_name, 'r') as file:
            for line in file:
                category, amount = line.split(":")
                expenses[category.strip()] = float(amount.strip())
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return expenses


def plot_expenses(expenses):
    categories = list(expenses.keys())
    amounts = list(expenses.values())

    # Pie charts drawn
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('expenses Distribution')
    plt.axis('equal')
    plt.show()

    # Plotting bar charts
    plt.figure(figsize=(8, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expenses Distribution')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.show()


def main():
    file_name = 'expenses.txt'
    expenses = read_expenses(file_name)

    if expenses:
        plot_expenses(expenses)


if __name__ == "__main__":
    main()
