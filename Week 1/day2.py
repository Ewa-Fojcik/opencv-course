numbers = [6, 9, 6, 7, 16]
print(numbers[0], numbers[-1])

total = 0
for num in numbers:
    print(num)
    total = total + num

average = total/len(numbers)
print(average)

print(max(numbers))
print(min(numbers))
print(sorted(numbers))