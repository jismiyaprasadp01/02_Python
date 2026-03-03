"""
The Banking System: Managing Accounts with OOP
Scenario:
Simulate a simple bank system: create accounts, deposit, withdraw, and check balances.

What you’ll learn:
Using classes for real-life simulations
Method design and data encapsulation

Task:
Log Session a BankAccount class with methods for deposit, withdraw, and balance check.

Example:
Start with balance 1000, deposit 500, withdraw 300, show balance.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-19
 
Expected Output:
1200
"""
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print(account.check_balance())
