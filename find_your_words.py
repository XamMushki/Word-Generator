from itertools import permutations
import pickle
from bisect import bisect_left


def binarySearch(l, w):
    i = bisect_left(l, w)
    if i != len(l) and l[i] == w:
        return w
    else:
        return -1


def load_and_find(word_to_find_list=[]):
    words_found_list = []
    actual_words_list = []

    word_to_find_list.sort()
    with open('words.bin', 'rb') as f:
        actual_words_list = pickle.load(f)

    for word in word_to_find_list:
        s = binarySearch(actual_words_list, word)
        if word == s:
            words_found_list.append(word)

        # if word in actual_words_list:
        #     words_found_list.append(word)
    # for word_to_find in word_to_find_list:
    #     first_char = word_to_find[0]
    #     direc = 'AlphaFiles/'
    #     name = direc + first_char + '.txt'
    #     words = list()
    #
    #     with open(name) as f:
    #         blob = f.read()
    #         words = blob.split(' ')
    #
    #     # ----------- LET'S FIND THE WORD ----------- #
    #     if word_to_find in words:
    #         words_found_list.append(word_to_find)
    return words_found_list


def generate_combinations(monkey_word):
    alpha_in_monkey_word = []
    for alpha in monkey_word:
        alpha_in_monkey_word.append(alpha)

    length = len(alpha_in_monkey_word)

    monkey_word_list = []
    for L in range(2, length + 1):
        for subset in permutations(alpha_in_monkey_word, L):  # Returns subset as tuple of characters
            s = ''
            for letter in subset:
                s += letter
            monkey_word_list.append(s)

    monkey_word_list_cleaned = []
    # removing the duplicates
    for word in monkey_word_list:
        if not word in monkey_word_list_cleaned:
            monkey_word_list_cleaned.append(word)
    return monkey_word_list_cleaned


def start_and_show(monkey_word):
    monkey_word_list = generate_combinations(monkey_word)
    words_found_list = load_and_find(monkey_word_list)
    if len(words_found_list) ==0:
        print('--- Sorry No Results Found! ---')
    else:
        words_found_list.sort()
        lengths = []
        for word in words_found_list:
            if not len(word) in lengths:
                lengths.append(len(word))
        lengths.sort()
        print('Results Found : ')
        for length in lengths:

            print('Word Length - ', length)
            for word in words_found_list:
                if len(word) == length:
                    print(word)


while True:
    print('\nEnter \'123\' to exit')
    print('Enter the letters without spaces or commas. like this --> paple or btae')
    monkey_word = input('Input >> ')
    if monkey_word == '123':
        print('Exit done')
        break
    start_and_show(monkey_word)
