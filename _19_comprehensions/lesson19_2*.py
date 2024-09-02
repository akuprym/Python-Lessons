# * Make transposed matrix  (поменять местами строки со столбцами)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed_matrix = []

for i in range(len(matrix)):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)

print(transposed_matrix)

# A shorter way (!!!) *

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed_matrix)