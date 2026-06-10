try:
    number = float(input("enter a number:"))
    result = 100/number
    print(result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("cant' devide by zero")
finally:
    print("program finished")