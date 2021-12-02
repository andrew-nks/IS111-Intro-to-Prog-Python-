with open("facilities.txt") as facility:
    facility_dict = {}
    room_list = []
    sch_list = []
    for line in facility:
        row = line.rstrip("\n").split("\t")
        sch = row[0]
        room = row[1]
        cap = row[2]
        projector = row[3]
        room_list.append([sch, room, cap, projector])
        if sch not in sch_list:
            sch_list.append(sch)

        for place in sch_list:
            filter_sch_list = []
            for data in room_list:
                if place == data[0]:
                    filter_sch_list.append([data[1], data[2], data[3]])
            facility_dict[place] = filter_sch_list

search_facility = input("Do you want to search for the facilities within a school? [Y|N]: ")
while search_facility == "Y":
    search_sch = input("Enter the school [LKCSB|SOE|SOL|SOA|SIS]: ")
    print(f"The following faciltiies are in {search_sch}:\n")
    print(f"Room #\t Cap\t Projector?")
    print(f"------\t---\t----------")
    for data in facility_dict[search_sch]:
        print(f"{data[0]}\t{data[1]}\t{data[2]}")
    search_facility = input("Do you want to search for the facilities within a school? [Y|N]: ")
print("Good-bye!")