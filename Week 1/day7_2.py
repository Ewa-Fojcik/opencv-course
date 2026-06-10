with open("students.txt", "w") as f:
    f.write("Anna,45\n")
    f.write("Marc,83\n")
    f.write("Ewa,34\n")
    f.write("Cristian,24\n")
    f.write("Andrea,92")


def get_result(grade):
    if grade >= 50:
        return("pass")
    else:
        return("fail")

highest_name = None
highest_grade = None

with open("students.txt", "r") as f:
    for line in f:
        splitted = line.strip().split(",")
        grade = float(splitted[1])
        results = get_result(grade)
        print(f"{splitted[0]} - {splitted[1]} - {results}")

        if highest_grade is None or highest_grade < grade:
            highest_grade = grade
            highest_name = splitted[0]

print(f'Highest score beongs to {highest_name}, who scored {highest_grade}')