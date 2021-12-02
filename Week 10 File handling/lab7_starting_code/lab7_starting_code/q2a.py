### Q2a: Universities 
# Write your code below:
def get_universities_founded_before(file, year):
    earlier_list = []
    with open(file, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            column = line.split("\t")
            founded = int(column[2])
            name = (column[0])
            
            if founded < year:
                earlier_list.append(name)

        return earlier_list

# print(get_universities_founded_before("universities-1.txt", 1905))