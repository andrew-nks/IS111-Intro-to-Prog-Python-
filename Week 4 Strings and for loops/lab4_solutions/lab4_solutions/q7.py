## Q7
# ################################################################################
# The functions below are for you to implement!
# Q7a 
def count_a(text):
    """
    This function takes in a piece of text (as a string) and returns the number 
    of times the word “a” occurs in the text. 

    You do not need to handle uppercase “A”. You can assume that each time the 
    word “a” occurs, both its previous character and its next character are a space.
    """
    # Modify the code below to return the number of "a" occurrences.
    # solution
    # the function is to count word 'a' not the letter 'a'
    count = 0
    for i in range(0, len(text)-2):
        if text[i]==' ' and text[i+1]=='a' and text[i+2]==' ':
            count += 1
    return count
    
# ################################################################################
# Q7b 
# solution
def count_an(text):
    """
    This function takes in a piece of text (as a string) and returns the number 
    of times the word “an” occurs in the text. 
    
    You do not need to handle uppercase “An”. You can assume that each time the 
    word “an” occurs, its previous character and its next character are both a space.
    """
    # Modify the code below to return the number of "an" occurrences.
    count = 0
    for i in range(0, len(text)-3):
        if text[i]==' ' and text[i+1]=='a' and text[i+2]=='n' and text[i+3]==' ':
            count += 1
    return count
