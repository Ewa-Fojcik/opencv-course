class product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0
    
    def apply_discount(self, percent):
        self.price = self.price - self.price*percent

    def display(self):
        if self.is_available() == True:
            print(f'{self.name} - {self.price} - in stock')
        else:
            print(f'{self.name} - {self.price} - out of stock')


p1=product("laptop",450,2)
p2=product("mouse",32,0)
p3=product("keyboard",200,8)
percent = 0.2
p1.apply_discount(percent)
p2.apply_discount(percent)
p3.apply_discount(percent)
p1.display()
p2.display()
p3.display()