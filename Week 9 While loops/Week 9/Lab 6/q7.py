def get_lineup(new_list):
    lineup = []
    for tup in new_list:
        for name in tup:
            if name == "":
                lineup.append(tup[0])
    while len(lineup) < len(new_list):
        for tup in new_list:
            for name in tup:
                if lineup.count(name) == 1 and name == tup[1] and tup[0] not in lineup:
                 lineup.append(tup[0])
                
    return lineup[::-1]


# info = [("Mary", "Jason"), ("John", "Alan"), ("Jason", "George"), ("Alan", "Christie"), ("Christie", "Mary"), ("George", "")]
# print(get_lineup(info))
