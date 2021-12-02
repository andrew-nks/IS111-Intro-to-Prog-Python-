from q5a import *

spam_dict = count_words_in_file("spam_sms.txt")

for key in spam_dict:
    if len(key) >= 4 and spam_dict[key] > 50:
        print(f"{key}\t: {spam_dict[key]}")