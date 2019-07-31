for i in range(4):
    for j in range(4):
        for k in range(3):
            print(i, j, k)

# nested loops challenge

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("X" * number)

# or

for x_count in numbers:
    output = '';
    for count in range(x_count):
        output += 'X'
    print(output)