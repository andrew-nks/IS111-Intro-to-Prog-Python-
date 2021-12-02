book_author_dict = {"Harry Potter and the Sorcerer's Stone":'J.K. Rowling', 
               "Turtles All the Way Down":'John Green',
               "Animal Farm and 1984":'George Orwell',
               "The Da Vinci Code":'Dan Brown',
               "Harry Potter and the Goblet of Fire":'J.K. Rowling',
               "Origin":'Dan Brown'}

search_author = input("Do you want to search for the author of a book? [Y|N] ")
while search_author == "Y":
    enter_title = input("Please enter a book title: ")
    result = ""
    for title, author in book_author_dict.items():
        if enter_title == title:
            result = author
    if result == "":
        print(f"Not found!")
    print(f"the author of the book is {result}")
    search_author = input("Do you want to continue? [Y|N] ")
