from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for i in range(len(words) - 2):
        words_pairs = (words[i], words[i + 1])
        if words_pairs not in chains:
            chains[words_pairs] = []
        chains[words_pairs].append(words[i + 2])

    #print chains    
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here
    link = choice(chains.keys())   # First key at random
    text += link[0] + " " + link[1] # Add that key in the text
    new_link = (link[1], choice(chains[link]))  # create the new key
    while(new_link in chains):
        text += " " + new_link[1]
        next_link = (new_link[1], choice(chains[new_link]))  # create the new key
        new_link = next_link

    text += " " + new_link[1]        

    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
