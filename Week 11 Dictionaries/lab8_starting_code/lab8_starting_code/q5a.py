## Q5a Word Counts
# write your code below
def count_words_in_file(new_file):
    new_dict = {}
    with open(new_file) as file:
        for line in file:
            row = line.rstrip("\n").split(" ")
            for word in row:
                    if word.lower() in new_dict:
                        new_dict[word.lower()] += 1
                    else:
                        new_dict[word.lower()] = 1

    return new_dict

