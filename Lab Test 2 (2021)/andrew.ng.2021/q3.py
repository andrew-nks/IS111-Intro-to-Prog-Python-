# Name:NG KAI SHEN ANDREW
# Email ID:    andrew.ng.2021
import datetime
def get_days_between(start_tup, end_tup):
    '''
    This function returns the number of days between two dates.
    Do not modify the code in this function!!!
    You're required to use this function in your code for Q3.
    
    Parameters:
        start_tup: the start date which is a tuple in the form (year, month, day).
             The year, month and day are integers.
        end_tup:   the end date. The format is the same as start_tup.

    Returns the number of days in between the 2 days (end_tuple – start_tuple).
    For example, if start_tup is (2020, 12, 1) and end_tup is (2020, 12, 3), this
    function returns the value 2.

    More examples:
    get_days_between((2021,10,15), (2021, 10, 30)) returns 15
    get_days_between((2021,8,15), (2021, 10, 11)) returns 57
    get_days_between((2021,8,15), (2021, 9, 12)) returns 28
    get_days_between((2021,10,15), (2021, 10, 29)) returns 14
    '''

    start_date = datetime.date(*start_tup)
    end_date = datetime.date(*end_tup)
    return (end_date - start_date).days


    
def get_vaccination_status(filename, today):
    
    pass
    # Write your code here.
    today = today.split("/")
    today = (int(today[2]), int(today[1]), int(today[0]))

    new_dict = {}
    with open(filename) as file:
        for line in file:
            row = line.rstrip("\n").split("|")
            id = row[0]
            age = int(row[1])
            first = row[2].split("/")
            second = row[3].split('/')

            if first != ["NA"]: 
                first_date = (int(first[2]), int(first[1]), int(first[0]))
            if second != ["NA"]:
                second_date = (int(second[2]), int(second[1]), int(second[0]))
            
            if age < 12:
                new_dict[id] = (age, False)
            
            elif first == ["NA"] or second == ["NA"]:
                new_dict[id] = (age, False)

            elif get_days_between(first_date, second_date) < 28:
                new_dict[id] = (age, False)

            elif get_days_between(first_date, second_date) > 56:
                new_dict[id] = (age, False)

            elif get_days_between(second_date, today) < 14:
                new_dict[id] = (age, False)

            elif age >= 12 and first != ["NA"] and second != ["NA"] and 28 <= get_days_between(first_date, second_date) <= 56 and get_days_between(second_date, today) >= 14:
                new_dict[id] = (age, True)

    return new_dict
            
    

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, filename, today, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_vaccination_status("{filename}", "{today}")')
        print()
        print(f'Expected: {expected_output}')
        result = get_vaccination_status(filename, today)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
        
    
    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, False), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(1, 'record1.txt', '25/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, True), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(2, 'record1.txt', '15/11/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, False), 'F1': (2, False), 'G2': (35, False), 'S2': (12, False), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(3, 'record1.txt', '15/1/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'F1': (2, False), 'S2': (11, False), 'S3': (8, False)}
    run_test_case(4, 'record2.txt', '15/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'G2': (35, False), 'S3': (22, False), 'S4': (62, False)}
    run_test_case(5, 'record3.txt', '1/11/2021' , expected_dict, "<class 'dict'>")
    
