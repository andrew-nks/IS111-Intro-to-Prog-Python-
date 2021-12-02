### Q5a: Matrix

# Write your code below:
def get_matrix(file):
    nested_rows = []
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
        return nested_rows


# get_matrix("matrix.txt")
