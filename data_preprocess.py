# In this program we simply collect all the words from the available word files in Files dir.
# and then removing the duplicates
# and then dump the words into words.bin file
# total number of words = 196631
# that means this program does not need to be executed unless any changes are made
# Driver code is at the end of this file.

import os
from collections import Counter
import pickle


def data_clean():
    direc = 'Files/'
    print(os.getcwd())
    files = [direc + file for file in (os.listdir('Files'))]

    word_list = []

    c = len(files)      # counter

    for file in files:
        with open(file, encoding='utf-8', errors='ignore') as f:
            word = f.read().lower()
            word_list += word.split()
        print(c)
        c -= 1
    for i in range(len(word_list)):
        if not word_list[i].isalpha():
            word_list[i] = ''

    dictionary = Counter(word_list)
    del dictionary['']

    words = []  # for final use

    for key, val in dictionary.items():
        _ = val
        words.append(key)
    return words


def save(sorted_words_list):
    with open('words.bin', 'wb') as f:
        pickle.dump(sorted_words_list, f)
    print('SAVED')


# print(words)
# print('words ', len(words))   # 196631

# DRIVER CODER

# words = data_clean()
# words.sort()
# save(words)

