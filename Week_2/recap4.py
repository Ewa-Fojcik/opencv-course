class Suspect():
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def __repr__(self):
        return f'Suspect ({self.name}, {self.age}, {self.status})'
    
    def is_active(self):
        if self.status == 'wanted':
            return True
        else:
            return False
    
    def display(self):
        if self.is_active() is True:
            print(f'{self.name} - age {self.age} - {self.status.upper()}')
        else:
            print(f'{self.name} - age {self.age} - {self.status}')


suspects = [
    Suspect('Aga', 24, 'wanted'),
    Suspect('Ewa', 30, 'cleared'),
    Suspect('Marta', 48, 'arrested'),
    Suspect('Toby', 80, 'cleared'),
    Suspect('Iga', 30, 'cleared')
]

def save_suspects(suspects, filename):
    with open(filename, 'w') as f:
        for i in suspects:
            f.write(f'{i.name},{i.age},{i.status}\n')

def load_suspects(filename):
    suspects = []
    with open(filename, 'r') as f:
        for line in f:
            stripped = line.strip().split(',')
            suspect = Suspect(stripped[0].strip(), float(stripped[1].strip()), stripped[2].strip())
            suspects.append(suspect)
        return suspects
    
save_suspects(suspects, "suspects.txt")
loaded = load_suspects("suspects.txt")
for s in loaded:
    if s.is_active():
        s.display()