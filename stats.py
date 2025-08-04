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

def sort_on(item):
    return item["num"]

def letter_sort(letter_dict):
    letter_list = []

    for letter in letter_dict:

        if letter.isalpha():
            letter_list.append({"char": letter, "num": letter_dict[letter]})

    letter_list.sort(key=sort_on, reverse=True)

    return letter_list
