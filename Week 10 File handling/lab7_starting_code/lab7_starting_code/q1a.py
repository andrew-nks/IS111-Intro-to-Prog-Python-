## Q1 Reading Files
# Write your code below:
##############################
def print_alternate_lines(file):
    with open(file, "r") as file:
        for i, line in enumerate(file):
            line = line.rstrip("\n")
            if i % 2 == 0:
                print(line)





