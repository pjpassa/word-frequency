import re
from collections import defaultdict


# Functions

# Takes a string, keeps characters and numbers, and lowercases them.
def reformat(text):
    text = re.sub(r'[\n]', " ", text)
    text = re.sub(r'[^A-Za-z1-9 ]', "", text)
    text = re.sub(r'[ *]', " ", text)
    text.lower()
    return text


# Takes a string and returns a defaultdict(int) histogram of the words
def word_frequency(file_text):
    file_text = reformat(file_text)
    word_list = file_text.split()
    histogram = defaultdict(int)
    for word in word_list:
        histogram[word] += 1
    return dict(histogram)


# Read file.
with open('sample.txt') as f:
    file_text = f.read()

histogram_dict = word_frequency(file_text)


# Create Dictionary.
# Keep top 20 words from dictionary.
# Print out the top 20 words.
