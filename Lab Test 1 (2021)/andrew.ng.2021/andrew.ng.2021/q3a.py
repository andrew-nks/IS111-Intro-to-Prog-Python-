# Name: Ng Kai Shen Andrew
# Email ID: andrew.ng.2021@scis.smu.edu.sg

def check_diversity(team):
    # Replace the code below with your implementation.
    boys = 0
    diff_races = []
    diff_religions = []
    for row in team:
        gender = row[1]
        race = row[2]
        religion = row[3]
        if gender == "M":
            boys += 1
        if race not in diff_races:
            diff_races.append(race)
        if religion not in diff_religions:
            diff_religions.append(religion)
    
    
    if boys == 1 or boys == 4 or boys == 0:
        return False
    elif len(diff_races) < 3:
        return False
    elif "Freethinker" in diff_religions:
        diff_religions.remove("Freethinker")
    elif len(diff_religions) < 2:
            return False
    
    return True

