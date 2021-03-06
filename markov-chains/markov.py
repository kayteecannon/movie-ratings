"""Generate Markov text from text files."""

from random import choice
import sys

# file_name = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(input_path)
    text = file.read()
    return text



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
        
        {Would, you} : [could, could, could, like, like]
    """
    full_text = open_and_read_file(input_path)
    full_text_lst = full_text.rstrip('\n').split()
    
    chains = {}

    for i in range(len(full_text_lst) - 2):
        # the next 3 lines will create a empty list and then appends the word at i(would) & i+1(you)
        key_list = []
        key_list.append(full_text_lst[i])
        key_list.append(full_text_lst[i + 1])

        key_tuple = tuple(key_list) #takes the key_list and convers it to a tuple {would, you}

        
        if key_tuple in chains.keys():
            chains.get(key_tuple).append(full_text_lst[i + 2])
        else:
            chains[key_tuple] = [full_text_lst[i + 2]]
        
                
    # for k, v in chains.items():
    #     print(f"{k}: {v})")

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""
    chains = make_chains(input_path)
      
    first_key = choice(list(chains.keys()))
    words = [first_key[0], first_key[1]]
    first_word = choice(chains[first_key])


    while first_word is not None:
        first_key = (first_key[1], first_word)
        words.append(first_word)
        first_word = choice(chains[first_key])        

    return ' '.join(words)


# Get the filepath from the user through a command line prompt, ex:
# python markov.py green-eggs.txt

input_path = sys.argv[1]

# This could also say something like:
#   input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
