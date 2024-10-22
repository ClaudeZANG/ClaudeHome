import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt


def load_users():
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as f:
            json.dump({}, f)
    with open('users.json', 'r') as f:
        return json.load(f)


def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)


def login(users):
    for _ in range(3):
        username = simpledialog.askstring("Login", "Enter your username:")
        pin = simpledialog.askstring("Login", "Enter your PIN:")
        if username in users and users[username]['pin'] == pin:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            return username
        else:
            messagebox.showwarning("Login Failed", "Invalid username or PIN. Try again.")
    messagebox.showerror("Login Failed", "Too many attempts. Exiting.")
    return None


def main_menu(users, username):
    if username == 'SysAdmin':
        admin_menu(users)
    else:
        user_menu(users, username)


def user_menu(users, username):
    while True:
        choice = simpledialog.askstring(
            "Menu",
            "Choose an option:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit"
        )
        if choice == "1":
            check_balance(users, username)
        elif choice == "2":
            deposit(users, username)
        elif choice == "3":
            withdraw(users, username)
        elif choice == "4":
            change_pin(users, username)
        elif choice == "5":
            save_users(users)
            messagebox.showinfo("Exit", "Thank you for using the ATM. Goodbye!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")


def admin_menu(users):
    while True:
        choice = simpledialog.askstring(
            "Admin Menu",
            "Choose an option:\n1. Add User\n2. Delete User\n3. Plot Balances\n4. Exit"
        )
        if choice == "1":
            add_user(users)
        elif choice == "2":
            delete_user(users)
        elif choice == "3":
            plot_balances(users)
        elif choice == "4":
            save_users(users)
            messagebox.showinfo("Exit", "Administrator logged out.")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")


def check_balance(users, username):
    balance = users[username]['balance']
    messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")


def deposit(users, username):
    amount = simpledialog.askfloat("Deposit", "Enter the amount to deposit:")
    if amount and amount > 0:
        users[username]['balance'] += amount
        messagebox.showinfo("Deposit Successful", f"${amount:.2f} has been added to your account.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a positive amount.")


def withdraw(users, username):
    amount = simpledialog.askfloat("Withdraw", "Enter the amount to withdraw (max $1000):")
    balance = users[username]['balance']
    if amount and 0 < amount <= 1000:
        if amount % 10 != 0:
            messagebox.showwarning("Invalid Amount", "Amount must be a multiple of $10.")
        elif balance >= amount:
            users[username]['balance'] -= amount
            messagebox.showinfo("Withdrawal Successful", f"${amount:.2f} has been withdrawn from your account.")
        else:
            messagebox.showwarning("Insufficient Funds", "Your balance is insufficient for this transaction.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid amount up to $1000.")


def change_pin(users, username):
    new_pin = simpledialog.askstring("Change PIN", "Enter your new 4-digit PIN:")
    if new_pin and len(new_pin) == 4 and new_pin.isdigit():
        users[username]['pin'] = new_pin
        messagebox.showinfo("PIN Changed", "Your PIN has been successfully changed.")
    else:
        messagebox.showwarning("Invalid PIN", "Please enter a valid 4-digit PIN.")


def add_user(users):
    new_user = simpledialog.askstring("Add User", "Enter the new username:")
    new_pin = simpledialog.askstring("Add User", "Enter the new 4-digit PIN:")
    if new_user and new_pin and len(new_pin) == 4 and new_pin.isdigit():
        if new_user in users:
            messagebox.showwarning("User Exists", "This username already exists.")
        else:
            users[new_user] = {"pin": new_pin, "balance": 0}
            messagebox.showinfo("User Added", f"User {new_user} has been added.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid username and PIN.")


def delete_user(users):
    user_to_delete = simpledialog.askstring("Delete User", "Enter the username to delete:")
    if user_to_delete in users and user_to_delete != 'SysAdmin':
        del users[user_to_delete]
        messagebox.showinfo("User Deleted", f"User {user_to_delete} has been deleted.")
    else:
        messagebox.showwarning("Invalid User", "Cannot delete this user.")


def plot_balances(users):
    usernames = [user for user in users if user != 'SysAdmin']
    balances = [users[user]['balance'] for user in usernames]
    plt.bar(usernames, balances)
    plt.xlabel('Users')
    plt.ylabel('Balance ($)')
    plt.title('User Account Balances')
    plt.show()


def main():
    users = load_users()
    root = tk.Tk()
    root.withdraw()  # Òþ²ØÖ÷´°¿Ú
    username = login(users)
    if username:
        main_menu(users, username)


if __name__ == "__main__":
    main()
