from marshal import load
def word_count(file_contents):
    word_list = file_contents.split()
    count = 0
    for words in word_list:
        count += 1
    return count

def letter_count(file_contents):
    letter_dict = {}
    for letter in file_contents.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict
