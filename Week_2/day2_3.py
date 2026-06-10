class Vehicle:
    def __init__(self, make, model, speed_kmh):
        self.make = make
        self.model = model
        self.speed_kmh = speed_kmh

    def __repr__(self):
        return f'Vehicle({self.make}, {self.model}, {self.speed_kmh})'
    
    def describe(self):
        return f'{self.make} {self.model} - top speed: {self.speed_kmh}'
    
    def is_fast(self):
        if self.speed_kmh > 200:
            return True
        else:
            return False


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, speed_kmh, battery_kwh):
        super().__init__(make, model, speed_kmh)
        self.battery_kwh = battery_kwh

    def __repr__(self):
        return f'ElectricVehicle({self.make}, {self.model}, {self.speed_kmh}, {self.battery_kwh})'
    
    def describe(self):
        return f'{self.make}, Model {self.model} - top speed: {self.speed_kmh}kmh - battery: {self.battery_kwh}kwh'
    

v1 = Vehicle("toyota", "yaris", 230)
v2 = Vehicle("BMW", "pretty bad", 5)
v3 = ElectricVehicle("Peugeot", "3", 500, 320)
v4 = ElectricVehicle("anotherone", "anothermake", 200, 100)

print(v1, v2, v3, v4)
print(v1.describe())
print(v2.describe())
print(v3.describe())
print(v4.describe())
print(v1.is_fast())
print(v2.is_fast())
print(v3.is_fast())
print(v4.is_fast())
