class Student():
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def add_grade(self, value):
        if value <0 or value>100:
            raise ValueError('Grade must be in the range of 0 to 100.')
        else:
            self.grade.append(value)
        return self.grade
    
    def calculate_average(self):
        grades_sum = 0
        for i in self.grade:
            grades_sum += i 
        return grades_sum/len(self.grade)
    
    def display(self):
        average = self.calculate_average()
        print(f"{self.name} - {self.subject} - average of: {average}")

students = [
    Student('Anna','Maths',[45,62,38]),
    Student('Ewa','Science',[90,88,95]),
    Student('Marek','Maths',[30,25,40]),
    Student('Sofia','History',[70,65,80]),
    Student('Tomek','Science',[55,48,20])
]

def save_students(students, filename):
    with open(filename, 'w') as f:
        for i in students:
            grades_str=",".join(str(g) for g in i.grade)
            f.write(f"{i.name},{i.subject},{grades_str}\n")

def load_students(filename):
    student_objects = []
    with open(filename, 'r') as f:
        for i in f:
            splitted = i.strip().split(",")
            grade = [int(g) for g in splitted[2:]]
            student = Student(splitted[0],splitted[1],grade)
            student_objects.append(student)
    return student_objects

saved = save_students(students, "students.txt")
loaded = load_students("students.txt")
for i in loaded:
    if i.calculate_average()<50:
        i.display()