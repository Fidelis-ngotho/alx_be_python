
class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount object with an optional initial balance.
        The balance defaults to zero if not provided.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
            
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        Return True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.__account_balance:
           
            return False
        else:
            self.__account_balance -= amount
           
            return True

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Your current balance is: {self.__account_balance:.2f}")
