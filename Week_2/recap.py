class Racer:
    def __init__(self, name, time, country):
        self.name=name
        self.time=time
        self.country=country

    def __repr__(self):
        return f"Racer({self.name}, {self.time}, {self.country})"
    
    def get_medal(self):
        if self.time < 60:
            return 'gold'
        elif self.time < 75:
            return 'silver'
        else:
            return 'bronze'
        
    def display(self):
        medal = self.get_medal()
        print(f'{self.name} ({self.country}) - {self.time} - {medal}')


R1 = Racer('Ewa', 58.3, 'Poland')
R2 = Racer('Patryk', 62, 'France')
R3 = Racer('Ola', 76, 'Germany')
R1.display()
R2.display()
R3.display()
            
