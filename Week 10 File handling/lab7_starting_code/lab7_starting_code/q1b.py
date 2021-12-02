### Q1b Reading Files
# Write your code below:
def print_alternate_columns(file):
    with open(file, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            columns = line.split("&")

            for i in range(len(columns)):
                if i % 2 != 0:
                    columns[i] = "&"

            for i in range(len(columns)):     
                if len(columns) < 3:
                    columns_string = str(columns[0])
                else:
                    columns = "".join(str(item) for item in columns)
                    columns_string = columns.rstrip("\t")
                
            print(columns_string)



