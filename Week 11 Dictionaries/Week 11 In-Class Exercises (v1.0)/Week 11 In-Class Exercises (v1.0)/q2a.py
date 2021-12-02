gpa_dict = {"George Leung": 3.4, "Eric Wong": 3.9, "Michelle Lee": 3.1}

def display_all_gpas(new_dict):
    print(f"Student Name\tStudent GPA")
    print(f"------------\t------------")
    for key in gpa_dict:
        print(f"{key}\t{gpa_dict[key]}")

# display_all_gpas(gpa_dict)