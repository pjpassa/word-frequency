import re
from collections import defaultdict


# Functions

# Takes a string, keeps characters and numbers, and lowercases them.
def reformat(text):
    text = re.sub(r'[\n]', " ", text)
    text = re.sub(r'[^A-Za-z1-9 ]', "", text)
    text = re.sub(r'[ *]', " ", text)
    text = text.lower()
    return text


# Takes a string and returns a dict histogram of the words.
def word_frequency(file_text):
    file_text = reformat(file_text)
    word_list = file_text.split()
    histogram = defaultdict(int)
    for word in word_list:
        histogram[word] += 1
    return dict(histogram)


# Takes a dictionary and returns a list of tuples of the top number of words.
def top_words(word_dictionary, number):
    word_list = []
    for key, value in word_dictionary.items():
        word_list.append((key, value))
    word_list.sort(key=lambda tuple_: -tuple_[1])
    return word_list[:number]


# Takes a list of tuples and prints them.
def print_results(word_list):
    for word, count in word_list:
        print("{} {}".format(word, count))

# Read file.
with open('sample.txt') as f:
    file_text = f.read()

# Create dictionary.
histogram_dict = word_frequency(file_text)

# Keep top 20 words from dictionary.
frequent_words = top_words(histogram_dict, 20)

# Print out the top 20 words.
print_results(frequent_words)
