class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        self.balance -= amount
    def display(self):
        print(self.balance)

account1 = BankAccount("Ewa", 500)

try:
    account1.deposit(-50)
except ValueError as e:
    print(e)

try:
    account1.withdraw(-20)
except ValueError as e:
    print(e)

account1.display()