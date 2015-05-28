import re


# Functions


# Takes a list of strings, joins them, and removes any punctuation.
def reformat(text):
    file_text = ' '.join(file_text)
    # Remove whitespace.
    file_text = re.sub(r'[^A-Za-z1-9 ]', "", file_text)
    file_text = re.sub(r'[ *]', " ", file_text)


# Read file.
with open('sample.txt') as f:
    file_text = f.readlines()

file_text = reformat(file_text)
# Create Dictionary.
# Keep top 20 words from dictionary.
# Print out the top 20 words.
