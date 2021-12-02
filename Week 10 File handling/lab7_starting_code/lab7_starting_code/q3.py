with open("temperatures.txt", "r") as file:
    import string
    for line in file:
        line = line.rstrip("\n")
        column = line.split("\t")
        print(column)
        # temp_list = []
        # for data in column:
        #     name = column[0]
        #     if not(data.isalpha()):
        #         temp_list.append(float(data))
        # max_temp = max(temp_list)
        # min_temp = min(temp_list)
        # print(f"{name}: {min_temp}, {max_temp}") 