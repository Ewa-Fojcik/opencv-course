class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print('insufficient funds')
    
    def display(self):
        print(f'{self.owner} - balance: ${self.balance}')


o1 = BankAccount("Ewa", 350)
o2 = BankAccount("Marta", 830)

o1.deposit(200)
o2.withdraw(300)
o1.display()
o2.display()

o2.deposit(2)
o1.withdraw(1000)
o1.display()
o2.display()

