

################################
#                              #
# Part 1: Messing with Strings #
#                              #
################################

def split_words(text):
    """
    Split an utterance on spaces
    
    Parameters:
        text (str): Running text with space-delimited words

    Returns:
        (list): A list of words

    Example:
        >>> split_words("This is an example.")
        ["This","is","an","example."]
    """
    x = text.split(" ")
    print(x)
    return

def caps_only(text):
    """
    Filter out all non-capitalized words from an utterance

    Parameters:
        text (str): Running text with space-delimited words

    Returns:
        (str): Running text with space-delimited words, all lowercase words removed
    """
    
    return


def make_box(message,buff,depth):
    """
    Make a fancy box of # around a string

    Parameters:
        message (str): Text to make a box around
        buff (int): number of white spaces between the string and inside edge of the box
        depth (int): how many # thick the box is

    Returns:
        (str): A string containing the boxed text
    """

    return


def inflect_ing(word):
    """
    Add -ing to the end of a word, enforcing American English rules of spelling
        If the word ends in a single consonant other than c, l, or y, double it before -ing,
        If the word ends in a single c, add a k before -ing,
        If the word ends in e, remove it before -ing,
        otherwise, just postpend -ing

    Parameters:
        word (str): A word (hopefully a verb)

    Returns:
        (str): Word with -ing appended
    """

    return



########################################
########################################
##                                    ##
##                                    ##
##  Part 2: Fun with Dicts and Lists  ##
##                                    ##
##                                    ##
########################################
########################################


def count_duplicates(seq):
    """
    Given a sequence, count how many distinct items appear multiple times. Use a set.

    Parameters:
        seq (list, tuple, or string): sequence which may contain duplicates

    Return:
        (int): number of duplicate items
    """
    return


def remove_duplicates(duplist):
    """
    Given a list, remove all the duplicate items. Use a set.

    Parameters:
        duplist (list): listwhich may contain duplicates

    Return:
        (list): contents of duplist with duplicates removed
    """

    return
    

def filter_by_index(original, indices):
    """
    Given a sequence and a sequence of indices i, 
    create a third tuple of the ith elements in the first sequence.
    Ignore indices out of range of the first list
    
    Parameters:
       original (list, tuple, or str): sequence of items
       indices (list or tuple of ints): 

    Return:
       (tuple): For every index i in indices, this should contain the ith element from original
    """

    return


def make_dict(keys, vals):
    """
    Make a dictionary out of a sequence of keys and a parallel sequence of values
    Do this with a for loop or a dict comprehension

    Parameters:
         keys (list, tuple, or string): A sequence of keys
         vals (list, tuple, or string): A sequence of values (len(keys) == len(vals))

    Returns:
         (dict): A dictionary of key:val for reach key[i]:val[i} in keys and vals
    """
    assert(len(keys) == len(vals))

    return


def make_dict_handleduplicates(keys, vals):
    """
    Make a dictionary out of a sequence of keys and a parallel sequence of values
    If a given key appears multiple times, it should map to a list of its values

    Parameters:
         keys (list, tuple, or string): A sequence of keys
         vals (list, tuple, or string): A sequence of values (len(keys) == len(vals))

    Returns:
         (dict): A dictionary of key:val for reach key[i]:[val[i},...] in keys and vals
    """
    assert(len(keys) == len(vals))

    return


####
#### Insert reverse_sort here for EC
####




