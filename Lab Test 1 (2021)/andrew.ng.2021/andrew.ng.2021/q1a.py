# Name: Ng Kai Shen Andrew
# Email ID: andrew.ng.2021@scis.smu.edu.sg

def get_area_difference(width1, length1, width2, length2):
    # Replace the code below with your implementation.
    area_one = int(width1 * length1)
    area_two = int(width2 * length2)

    if area_one > area_two:
        return area_one - area_two
    elif area_two > area_one:
        return area_two - area_one
    else:
        return 0