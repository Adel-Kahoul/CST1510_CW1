"""
Create a class BankAccount with owner and balance (default 0) and methods:

deposit(amount)
withdraw(amount) – refuse the withdrawal and print a message if there is not enough money
show_balance()
Test it with several deposits and withdrawals, including one that should fail.
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal of", amount, "refused: not enough money")
        else:
            self.balance -= amount
            print("Withdrew", amount)

    def show_balance(self):
        print(self.owner + "'s balance:", self.balance)


account = BankAccount("Tony")
account.show_balance()

account.deposit(150)
account.withdraw(120)
account.show_balance()

