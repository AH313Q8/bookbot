def word_count(file_contents):
    word_list = file_contents.split()
    count = 0
    for words in word_list:
        count += 1
    return count
