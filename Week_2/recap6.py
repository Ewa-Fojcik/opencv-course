class Password():
    def __init__(self, username, password):
        self. username = username
        self.password = password
    
    def is_strong(self):
        return len(self.password)>=8 and any(c.isdigit() for c in self.password)

    def display(self):
        strength = self.is_strong()
        print(f'{self.username} - {"strong" if strength else "weak"} password')
users = [
    Password('Ewa', 'Hellooooooo1'),
    Password('Henry', 'hola')
]

for user in users:
    user.display()