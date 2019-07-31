numbers = [20, 63, 52, 20, 45, 20]

# add number to the list
numbers.append(10)
print(numbers)

# insert a number in the list,first parameter is the location,second is the name
numbers.insert(2, 102)
print(numbers)

# remove a number in the list
numbers.remove(63)
print(numbers)

# pop a number from the list
numbers.pop()
print(numbers)

# find the index of a number
print(numbers.index(45))

# check if a number exist
print(60 in numbers)

# counting the occurence of a number
print(numbers.count(20))

# swap a list we use sort
numbers.sort()   # prints in ascending order
print(numbers)

numbers.reverse() # prints in descending order
print(numbers)
# copy a list
numbers2 = numbers.copy()
print(numbers2)

# clear numbers in the list
numbers.clear()
print(numbers)


# challenge write a program to remove the duplicate

list = [20, 63, 52, 20, 45, 20]
unique = []
for num in list:
    if num not in unique:
        unique.append(num)
print(unique)