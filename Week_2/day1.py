class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_result(self):
        if self.grade >= 50:
            return "pass"
        else:
            return "fail"
        
    def display(self):
        result = self.get_result()
        print(f'{self.name} - {self.grade} - {result}')
            
    def summary(self):
        result = self.get_result()
        return(f'{self.name} scored {self.grade} and got: {result}')

    
s1=Student("Anna", 45)
s2=Student("Ewa", 24)
s3=Student("Maggs", 82)
s1.display()
s2.display()
s3.display()

s1_summary = s1.summary()
print(s1_summary)

            
