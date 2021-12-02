def get_unique_titles(book_list):
    new_list = []
    for row in book_list:
        title = row[0]

        if title not in new_list:
            new_list.append(title)

    return new_list

print(get_unique_titles([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4)]))