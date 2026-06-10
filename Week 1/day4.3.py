def get_student():
    name = input(f'gimme your name')
    s1 = float(input(f'gimme score no 1'))
    s2 = float(input(f'gimme score no 2'))
    s3 = float(input(f'gimme score no 3'))
    return name, s1, s2, s3

def calc_average(s1, s2, s3):
    average = (s1+s2+s3)/3
    return average

def get_grade(average):
    if average > 60:
        return 'pass'
    else:
        return 'fail'
    
def display_report(name, average, grade):
    print(f'Student {name} | average {average} | grade: {grade}')

name, s1, s2, s3 = get_student()
average = calc_average(s1, s2, s3)
grade = get_grade(average)
report = display_report(name, average, grade)