class BankAccount:
    def __init__(self, initial_balance=100):  # Accept an initial balance
        self.account_balance = initial_balance  # Set the balance to the initial value

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")
