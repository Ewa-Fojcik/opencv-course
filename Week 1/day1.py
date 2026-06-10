name = "Ewa"
age = 24
height = 172.8
freelance = True

print(f'{name} is {age} years old and {height} centemiters tall. freelance: {freelance}')

print(type(name))
print(type(age))
print(type(height))
print(type(freelance))


height_2 = int(input("what's is your height in centemeters?"))
weight_2 = float(input("What's your weight?"))

BMI = weight_2 / ((height_2/100)**2)
print(f"your BMI is {round(BMI, 2)}")