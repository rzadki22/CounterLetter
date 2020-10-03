"Napisz funkcję, która zlicza wystąpienia liter w podanym tekście."

###############################################################################

from typing import Dict
from collections import defaultdict, Counter

def count_letters_1(text: str) -> Dict[str, int]:
    """
    Wariant bez wykorzystania defaultdict
    """
    letter_dict = {}
    for key in sorted(set(text)):
        letter_dict[key] = text.count(key)
    return letter_dict


a_1 = count_letters_1('abc')

a_2 = count_letters_1('aabcccc')

a_3 = count_letters_1('ala ma kota')

###############################################################################

def count_letters_2(text: str) -> Dict[str, int]:
    letter_dict = defaultdict(int)
    for letter in text:
        letter_dict[letter] += 1
    return letter_dict
        

b_1 = count_letters_2('abc')

b_2 = count_letters_2('aabcccc')

b_3 = count_letters_2('ala ma kota')

###############################################################################

def count_letters_3(text: str) -> Dict[str, int]:
    letter_dict = Counter(text)
    return letter_dict
        

c_1 = count_letters_3('abc')

c_2 = count_letters_3('aabcccc')

c_3 = count_letters_3('ala ma kota')