# with open("facilities.txt") as facilities:
#     new_list = []
#     school_list = []
#     school_dict = {}
#     for line in facilities:
#         row = line.rstrip("\n").split("\t")
#         sch = row[0]
#         room = row[1]
#         cap = row[2]
#         projector = row[3]
#         new_list.append([sch, room, cap, projector])
#         if sch not in school_list:
#             school_list.append(sch)

#         for place in school_list:
#             room_dict = {}
#             for data in new_list:
#                 if place == data[0]:
#                    room_dict[data[1]] = [data[2], data[3]]
#             for key in room_dict:    
#                 if room_dict[key][1] == "yes":
#                     room_dict[key][1] = "has"
#                 else:
#                     room_dict[key][1] = "does not have"
#             school_dict[place] = room_dict
#     print(school_dict)

# search_facility = input("Do you want to search for a facility? [Y|N] :")
# while search_facility == "Y":
#     search_sch = input("Enter the school [LKCSB|SOE|SOE|SOA|SIS : ")
#     search_room = input("Enter room number: ")
#     print(f"{search_sch} has a capacity of {school_dict[search_sch][search_room][0]} and {school_dict[search_sch][search_room][1]} a projector")
#     print("\n")
#     search_facility = input("Do you want to continue the search? [Y|N] : ")
# print(f"Thanks for using the system!")
    
        



