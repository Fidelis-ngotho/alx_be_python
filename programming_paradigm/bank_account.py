import os

class BankAccount:
    def __init__(self):
        self.file_path = 'balance.txt'
        self.account_balance = self.load_balance()

    def load_balance(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return float(file.read())
        return 0.0  # Default balance if file doesn't exist

    def save_balance(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.account_balance))

    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()  # Save the updated balance
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.save_balance()  # Save the updated balance
            print(f"Withdrew: ${amount:.1f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")
