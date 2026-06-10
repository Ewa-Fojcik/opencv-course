class Racer():
    def __init__(self, name, country, time):
        self.name = name
        self.country = country
        self.time = time

    def __repr__(self):
        return f"Racer ({self.name}, {self.country}, {self.time})"
    
    def get_medal(self):
        if self.time < 60:
            return "gold"
        elif self.time < 75:
            return "silver"
        else:
            return "bronze"
    
    def display(self):
        print(f'{self.name} ({self.country}) - {self.time} - {self.get_medal()}')


racers = [
    Racer('Ewa', 'Poland', 52),
    Racer('Mike', 'US', 63),
    Racer('Leo', 'Czech', 89)]

def save_results(racers, filename):
    with open(filename, 'w') as f:
        for i in racers:
            f.write(f"{i.name},{i.country},{i.time}\n")

def load_results(filename):
    racers = []
    with open(filename, "r") as f:
        for line in f:
            splitted = line.strip().split(",")
            racer = Racer(splitted[0], splitted[1], float(splitted[2]))
            racers.append(racer)
        return racers
            
save_results(racers, "results.txt")
loaded = load_results("results.txt")
for racer in loaded:
    racer.display()
