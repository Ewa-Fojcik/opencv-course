class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.pages} pages)'
    def summary(self):
        return(f'{self.title} by {self.author} - {self.pages}')

class AudioBook(Book):
    def __init__(self, title, author, duration_hours):
        super().__init__(title, author, 0)
        self.duration_hours = duration_hours
    def __repr__(self):
        return f'AudioBook({self.title}, {self.author}, {self.duration_hours})'
    def summary(self):
        return(f'{self.title} by {self.author} - {self.duration_hours} hours')
    
b1 = Book("mybook","Ewa", 752)
b2 = Book("h potter","JK Rawling", 394)
a1 = AudioBook("idkwhat","idkwho", 67)
a2 = AudioBook("another one", "Freddie", 101)

print(b1,b2,a1,a2)
print(b1.summary())
print(b2.summary())
print(a1.summary())
print(a2.summary())

