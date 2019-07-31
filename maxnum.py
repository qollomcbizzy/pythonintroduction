numbers = [10, 3, 20, 21, 62, 2, 42]
# lets find the maximum number in the list

max = numbers[0]
for number in numbers:
    if number > max:
        max =  number
print(max)

# find the minimum number in the list

min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print(min)