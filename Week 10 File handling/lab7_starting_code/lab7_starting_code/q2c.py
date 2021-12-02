### Q2c: Universities 
# Write your code below:
def search_with_keyword(file, keyword):
    new_list = []
    with open(file, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            column = line.split("\t")
            school = column[0]
            acronym = column[1]
            if keyword.lower() in line.lower():
                new_list.append(acronym)
    return new_list

