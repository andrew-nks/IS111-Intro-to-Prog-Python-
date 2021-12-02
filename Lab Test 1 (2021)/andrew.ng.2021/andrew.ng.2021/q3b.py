# Name: Andrew Ng
# Email ID: andrew.ng.2021

import q3a

def swap_members(team1, team2):
    # Replace the code below with your implementation.
    for row in team1:
        boys1 = 0
        diff_races1 = {}
        number_race = 0
        diff_religions1 = []
        gender = row[1]
        race = row[2]
        religion = row[3]
        if gender == "M":
            boys1 += 1
        if race not in diff_races1:
            diff_races1.append(race)
        if race in diff_races1:
            number_race += 1
            diff_races1.append(number_race)
        if religion not in diff_religions1:
            diff_religions1.append(religion)

    return diff_races1

              
    # for row in team2:
    #     boys2 = 0
    #     diff_races2 = []
    #     diff_religions2 = []
    #     gender = row[1]
    #     race = row[2]
    #     religion = row[3]
    #     if gender == "M":
    #         boys2 += 1
    #     if race not in diff_races2:
    #         diff_races2.append(race)
    #     if religion not in diff_religions2:
    #         diff_religions2.append(religion)

    # if len(diff_races1) < 3 and len(diff_races2) > 3:
            
    #         ans = []
    #         for i, v in enumerate(team1):
    #             for index, value in v:
    #                 if value[2] == max():
    #                     ans.append(value[0])
            
    #         for i, v in enumerate(team2):
    #             for index, value in v:
    #                 if value

team1 = [('Xavier', 'M', 'Chinese', 'Freethinker'), 
         ('Faith', 'F', 'Chinese', 'Christianity'),
         ('Li Wen', 'F', 'Chinese', 'Freethinker'),
         ('Siti', 'F', 'Malay', 'Islam'),
         ('Nicholas', 'M', 'Chinese', 'Freethinker')]
team2 = [('Ismail', 'M', 'Malay', 'Islam'),
         ('Boon Kiat', 'M', 'Chinese', 'Christianity'),
         ('Benjamin', 'M', 'Eurasian', 'Christianity'),
         ('Sajid', 'M', 'Indian', 'Islam'),
         ('Aisha', 'F', 'Malay', 'Islam')]