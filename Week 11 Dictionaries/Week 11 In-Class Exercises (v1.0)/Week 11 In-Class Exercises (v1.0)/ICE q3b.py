def read_into_dict(file):
    with open(file) as new_file:
        new_dict = {}
        for line in new_file:
            line = line.rstrip("\n")
            row = line.split("\t")
            key = row[0]
            value = row[1]
            if key not in new_dict:
                new_dict[key] = value
        return new_dict

print(read_into_dict("email_IDs.txt"))