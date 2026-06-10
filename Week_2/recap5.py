class Car():
    def __init__(self, make, model, milage):
        self.make = make
        self.model = model
        self.milage = milage

    def __repr__(self):
        return f'Car({self.make}, {self.model}, {self.milage})'
    
    def needs_service(self):
        if self.milage > 100000:
            return True
        else:
            return False
    
        
    def display(self):
        service = self.needs_service()
        print(f'{self.make} {self.model} - {self.milage}km - service: {"yes" if service else "no"}')


cars = [
    Car('Toyota', 'Corolla', 45),
    Car('Honda', 'Civic', 500),
    Car('model1', 'make1', 100000),
    Car('model2', 'make2', 1000000),
    Car('model3', 'make3', 5)
]

def save_cars(cars, filename):
    with open (filename, 'w') as f:
        for i in cars:
            f.write(f"{i.make},{i.model},{i.milage}\n")

def load_cars(filename):
    car_objects = []
    with open (filename, 'r') as f:
        for i in f:
            splitted = i.strip().split(",")
            car=Car(splitted[0], splitted[1], int(splitted[2].strip()))
            car_objects.append(car)
    return car_objects


            
save_cars(cars, 'cars.txt')
loaded=load_cars('cars.txt')
for car in loaded:
    if car.needs_service():
        car.display()


