from random import choice
from sys import argv

def open_and_read_file(file_path1,file_path2=""):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    if file_path2:
        contents = open(file_path1).read() + open(file_path2).read()
    else:
        contents = open(file_path1).read()    

    return contents


def make_chains(text_string,n):
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
    for i in range(len(words) - n):
        words_list = []

        for j in range(n):
            words_list.append(words[i+j])
        words_keys = tuple(words_list)
        #print words_keys  #Used for debugging
        

        if words_keys not in chains:
            chains[words_keys] = []
        chains[words_keys].append(words[i + n])
    print chains  # Used for debugging    
    return chains


def make_text(chains,n):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    new_list_key = []
    next_list_key = []


    # your code goes here
    while(True):
        link = choice(chains.keys())   # First key at random
        if link[0][0].isupper():
            for i in range(len(link)):
                text += link[i] + " " # Add that key in the text
            break 
    #print text 

    # Creating a new key tuple
    for i in range(1,n): 
        new_list_key.append(link[i])
    new_list_key.append(choice(chains[link]))
    new_link = tuple(new_list_key)  # create the new key

    while(new_link in chains):
        for i in range(len(new_link)):
            text += new_link[i] + " " # Add that key in the text


        for i in range(1,n): 
            next_list_key.append(new_link[i])
        next_key_tup = tuple(next_list_key)
        next_link = (next_key_tup, choice(chains[new_link]))  # create the new key

        new_link = next_link

    #for i in range(len(new_link)):
    #    text += new_link[i] + " " # Add that key in the text
    #text += " " + new_link[1]        

    return text


input_path1 = argv[1]


# Open the file and turn it into one long string
if len(argv) < 3:
    input_text = open_and_read_file(input_path1)
else:
    input_text = open_and_read_file(input_path1,argv[2])    

# Get a Markov chain
chains = make_chains(input_text,2)

# Produce random text
random_text = make_text(chains,2)

print random_text
