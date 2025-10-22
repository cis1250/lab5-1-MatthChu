#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
def get_sentence(s):
    s = str(input("Enter a sentance: "))
    return s

def calculate_frequencies(sentence):
    words = []
    count = []
    user_sentence = sentence.split()

    for word in user_sentence:  # iterate over words, not characters
        nosym = ""
        for char in word:
            if char.isalnum():  # keep only letters and numbers
                nosym += char
        nosym = nosym.lower()  # convert to lowercase

        if nosym:  
            if nosym in words:  
                index = words.index(nosym)
                count[index] += 1
            else:
                words.append(nosym)
                count.append(1)
    return words, count

def print_frequencies(words, count):
    for i in range(len(words)):
        print(words[i], ":", count[i])
        
def main ():
    sentance = ""
    count = []
    words = []
    while True:
        sentance = get_sentence(sentance)
        if is_sentence(sentance):
            break
        else:
            print("Enter a valid sentance")
    words, count = calculate_frequencies(sentance)
    print_frequencies(words, count)


main()

