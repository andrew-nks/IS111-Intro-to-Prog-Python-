# import q2a
def get_titles_and_counts(book_list):
    new_list = []
    for row in book_list:
        title = row[0]
        number = row[3]
        if title not in new_list:
            new_list.append(title)
            new_list.append(number)
        else:
            for i, row in enumerate(new_list):
                if title == row:
                    new_list[i+1] += number # i + 1 because the amount is to the right of title
    
    return new_list
            


print(get_titles_and_counts([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4), ("Intro to Python", "Ed-3", "hardcover", 3)]))
