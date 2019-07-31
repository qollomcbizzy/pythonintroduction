matrix = [
    [1, 2, 3],
    [4, 6, 7],
    [8, 9, 5]
]

# prints the number in the first row,second column

print(matrix[0][1])
print(matrix[1][0])

#  modify the list
matrix[0][1] = 11
print(matrix[0][1])


# loop over the items
# start with a row

for row in matrix:
    for col in row:
        print(col)
