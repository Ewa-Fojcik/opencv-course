class Expense():
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def add_expenses(self):
        if self.amount >= 0:
            total_expenses += self.amount
        else:
            raise ValueError("Amount can't be in negative numbers")
        return total_expenses
    
    def category_spending(self):
        for i in self.category:
            total_expenses += self.amount(i)
        return total_expenses
    def display(self):
        for i in self.category:
            print(f"expenses for {i}:  {self.category_spending}")

expenses = [
    Expense('Pizza',50,'food'),
    Expense('Bus ticket',10,'transport'),
    Expense('Movie',15,'entertainment'),
    Expense('Groceries',120,'food'),
    Expense('Taxi',25,'transport'),
    Expense('Concert',80,'entertainment'),
    Expense('Coffee',5,'food')
]


def save_expenses(expenses, filename):
    with open(filename, 'w') as f:
        for i in expenses:
            f.write(f"{i.description},{i.amount},{i.category}\n")

def load_expenses(filename):
    expenses_objects = []
    with open(filename, 'r') as f:
        for i in f:
            splitted = i.strip().split(",")
            expenses = Expense(splitted[0],int(splitted[1]),splitted[2])
            expenses_objects.append(expenses)
        return expenses_objects
    
saved = save_expenses(expenses, 'expenses.txt')
loaded = load_expenses('expenses.txt')

Expense.category_spending('food')