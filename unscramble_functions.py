"""CSC108: Fall 2021 -- Assignment 1: Unscramble

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Tom Fairgrieve, Sadia Sharmin, and 
Jacqueline Smith.
"""

# Move constants
SHIFT = 'S'
FLIP = 'F'
CHECK = 'C'

# Constant for hint functions
HINT_MODE_SECTION_LENGTH = 3


def get_section_start(section_num: int, section_len: int) -> int:
    """Return the starting index of the section corresponding to section_num
    if the length of a section is section_len.

    >>> get_section_start(1, 3)
    0
    >>> get_section_start(2, 3)
    3
    >>> get_section_start(3, 3)
    6
    >>> get_section_start(4, 3)
    9
    """
    return (section_num - 1) * section_len
    # Write your code for get_section_start here


# Write the rest of your functions here
def is_valid_move(step: str) -> bool:
    """ return the parameter of step equal to 'S','F' and 'C'
    >>> is_valid_move('S')
    True
    >>> is_valid_move('F')
    True
    >>> is_valid_move('C')
    True
    >>> is_valid_move('D')
    False
    """
    if step == 'S':
        return True
    elif step == 'F':
        return True
    elif step == 'C':
        return True
    else:
        return False


def get_num_sections(string_answer: str, section_len: int) -> int:
    """ return the number of sections in the answer string based on the
    values of the parameters

    >>> get_num_sections("apples", 3)
    2
    >>> get_num_sections("pineapple", 3)
    3
    """
    return int(len(string_answer) / section_len)


def is_valid_section(num: int, string_answer: str, section_len: int) -> bool:
    """ return True if and only if the parameter represents a section number
    that is valid for the given answer string and section length

    >>> is_valid_section(2, "apples", 3)
    True
    >>> is_valid_section(3, "apples", 3)
    False
    """
    if num >= 1 and num <= len(string_answer) / section_len:
        return True
    else:
        return False


def check_section(game_state: str, answer_string: str, valid_section: int, section_length: int) -> bool:
    """return True if and only if the specified section in the game state matchs
    the same section in the answer string. 

    >>> check_section("apples",'les',2, 3)
    True
    >>> check_section("apples",'ple',2, 3)
    False

    """



#

def change_section(game_sate: str, applied_move: str, section_num: int, section_length: int) -> str:
    """return a new string that reflects the updated game state after applying the given move

    >>> change_section("appsel",'F',2,3)
    'apples'
    >>> change_section('teerkocrlkae','F',2,4)
    'teerrocklkae'
    """



#

def section_needs_flip(game_state: str, answer_string: str, valid_section_num: int) -> bool:
    """return True if and only if the specified section in the game state will never match the same
    section in the answer string without doing a FLIP move

    >>> section_needs_flip("ACT","CAT",1)
    True

    >>> section_needs_flip("faterh","father",2)
    False

    >>> section_needs_flip("fatreh","father",2)
    True

    """



#

def get_move_hint(game_state: str, answer_string: str, scrambled_section_num: int) -> str:
    """Return a move that will help user come closer to the solving the section
    with the index scrambled_section_num in the str game_state coming to the answer answer_string
    >>> get_move_hint("CAT","ATC",1)
    'S'

    >>> get_move_hint("Father","Fatreh",2)
    'F'

    """
    ans = ""
    if section_needs_flip(game_state,answer_string,scrambled_section_num) == True:
        return 'F'
    else:
        return 'S'





