import re
import sys
from collections import defaultdict


# Functions

# Takes a string, keeps characters and numbers, and lowercases them.
def reformat(text, regex=r'[^A-Za-z1-9 ]'):
    text = re.sub(r'[\n]', " ", text)
    text = re.sub(regex, "", text)
    text = re.sub(r'[ *]', " ", text)
    text = text.lower()
    return text


# Takes a string and returns a dict histogram of the words.
def word_frequency(file_text):
    file_text = reformat(file_text)
    word_list = file_text.split()
    histogram = defaultdict(int)
    with open("ignored_words.txt") as f:
        ignored_words = f.read()
    ignored_words = reformat(ignored_words, r'[^A-Za-z1-9,]')
    ignored_list = ignored_words.split(",")
    for word in word_list:
        if word not in ignored_list:
            histogram[word] += 1
    return dict(histogram)


# Takes a dictionary and returns a list of tuples of the top number of words.
def top_words(word_dictionary, number):
    word_list = [x for x in word_dictionary.items()]
    word_list.sort(key=lambda tuple_: -tuple_[1])
    return word_list[:number]


# Takes a list of tuples and prints them.
def print_results(word_list):
    max_word_length = max(len(pair[0]) for pair in word_list)
    scale = word_list[0][1]/50
    for word, count in word_list:
        count_text = "#"*int(round(count/scale))
        word_text = word + " "*(max_word_length - len(word))
        print("{} {}".format(word_text, count_text))

# Read file.
with open(sys.argv[1]) as f:
    file_text = f.read()

# Create dictionary.
histogram_dict = word_frequency(file_text)

# Keep top 20 words from dictionary.
frequent_words = top_words(histogram_dict, 20)

# Print out the top 20 words.
print_results(frequent_words)
