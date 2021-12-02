## Q4 Students and Schools
# write your code below
student_to_school_dict = {'Joe Tan':'SIS', 'Alan Lee':'SOE', 'George Wong':'SOSS', 'Liu Chee Hwa':'SOL', 'Ng Yew Tung':'SIS', 'Wendy Li':'SIS', 'Jerry Lim':'SOSS'}

def get_students_by_school(my_dict):
    new_dict = {}
    sch_list = []
    for key in my_dict:
        if my_dict[key] not in sch_list:
            sch_list.append(my_dict[key])
    
    for sch in sch_list:
        list_by_sch = []
        for key in my_dict:
            if my_dict[key] == sch:
                list_by_sch.append(key)
        new_dict[sch] = list_by_sch
    
    return new_dict
            

print(get_students_by_school(student_to_school_dict))




