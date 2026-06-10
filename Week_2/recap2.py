class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Woof! I'm a {self.name}"
    
    def __repr__(self):
        return f"dog({self.name}, {self.breed})"
    
dog1 = Dog('rex', 'pinczer')
dog2 = Dog('oskar', 'labradr')

print(dog1, dog2)
print(dog1.bark())
print(dog2.bark())