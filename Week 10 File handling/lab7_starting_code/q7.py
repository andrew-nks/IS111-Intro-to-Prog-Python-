def scramble_word(word):
    import random
    new_word = word
    element = word[1:-1]                                  # exclude 1st and last letter
    if len(element) == 2:                                   # if only 2 middle letters e.g "ai" in "said"
        if element[0] == element[1]:                        # if both letters are the same e.g "oo" in "good"
            return word
    if len(word) > 3:
        while new_word == word:                               # if new word is same, scramble again
            scrambled_word = []
            shuffle_element = "".join(random.sample(element, len(element))) # shuffle middle letters, make string
            scrambled_word.append(word[0])
            scrambled_word.append(shuffle_element)
            scrambled_word.append(word[-1])                   # put 1st, scrambled letters, last in a list

            new_word = "".join(scrambled_word)                # completed scrambled word  
    return new_word


def scramble_word_symbol(word):
    last_ch = word[-1]
    word = word[:-1]                                # e.g "can."" return "can" ; "as." return "as"
    new_word = scramble_word(word) + last_ch

    return new_word



def scramble_word_apostrophe(word):
    i = word.index("'")                   # index of symbol
    ending = word[i+1:]                     # e.g "can't." return "t."
    word = word[:i+1]                       # e.g "can't." return "can'"
    new_word = scramble_word(word) + ending

    return new_word

def check_digit(word):
	    for ch in word:
             if ch.isdigit():
                return False

scrambled_row = []
for word in data:
    if word != "" and word != " " and check_digit(word) != False:  
        if "'" in word:                                                      # find words with '
            scrambled_row.append(scramble_word_apostrophe(word))
        elif word[-1] in ",.?/%'!&*-_()":                                   # find words ending with symbol
            scrambled_row.append(scramble_word_symbol(word))
        else:
            scrambled_row.append(scramble_word(word))
print(scrambled_row)