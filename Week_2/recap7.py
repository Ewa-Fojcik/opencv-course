
try:
    number = float(input("Enter a number: "))
    result = 100/number
    print(result)
except ValueError:
    print("thats not a number")
except ZeroDivisionError:
    print ("cant devide by 0")
finally:
    print("program finished")