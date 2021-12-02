### Q5b: Matrix

# Write your code below:
def get_matrix_transpose(file):
    nested_rows = []
    nested_transposed_rows = []
    with open(file) as matrix:
        for line in matrix:
            line = line.rstrip("\n")
            row = line.split("\t")
            row_list = []
            for data in row:
                for digit in data:
                    if digit.isdigit():
                        row_list.append(float(digit))

            nested_rows.append(row_list)

        for data in nested_rows:
            transposed_row = []
            for i, set in enumerate(nested_rows):
                transposed_row.append(set.pop(0))
            nested_transposed_rows.append(transposed_row)
    
    return nested_transposed_rows

# print(get_matrix_transpose("matrix.txt"))

def transpose(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        nested_list = []
        for row in matrix:
            new_list = []
            for i, value in enumerate(matrix):
                new_list.append(value.pop(0))
            nested_list.append(new_list)
        return nested_list    
    
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
