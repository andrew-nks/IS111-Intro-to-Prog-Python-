with open("employees.txt") as employees:
    employee_dict = {}
    id_list = []
    employee_list = []
    for line in employees:
        row = line.rstrip("\n").split("\t")
        for i, word in enumerate(row):
            if ":" in word:
                word = word[i]
            print(word)

        