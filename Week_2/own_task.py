class Books():
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
    def is_borrowed(self):
        return self.availability
    def borrow(self):
        if self.is_borrowed():
            print("already borrowed")
        else:
            self.availability = True
        return self.availability
    def return_book(self):
        if self.is_borrowed():
            self.availability = False
        else:
            print('This book is available')
        return self.availability
    def display(self):
        borrowed = self.is_borrowed()
        print(f"{self.title} - {self.author} - {'not available' if borrowed else 'available'}")

def load_library(filename):
    library_objects = []
    with open(filename, 'r') as f:
        for i in f:
            splitted = i.strip().split(",")
            book = Books(splitted[0], splitted[1], splitted[2] == "True")
            library_objects.append(book)
    return library_objects

def save_library(books, filename):
    with open(filename, 'w') as f:
        for book in books:
            f.write(f"{book.title},{book.author},{book.availability}\n")

loaded = load_library('week_2/books.txt')
for i in loaded:
    if i.is_borrowed() is False:
        i.display()

loaded[0].borrow()
loaded[0].display()

loaded[0].return_book()
loaded[0].display()

save_library(loaded, 'week_2/books.txt')