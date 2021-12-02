### Q2b: Universities 
# Write your code below:
def get_average_num_students(file):
    with open(file, "r") as file:
        total_students = 0
        count = 0
        for line in file:
            line = line.rstrip("\n")
            column = line.split("\t")
            students = int(column[3])
            total_students += students
            count += 1
 
        return total_students / count