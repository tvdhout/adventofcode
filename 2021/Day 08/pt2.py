import numpy as np
from typing import List, Set

with open('input.txt') as file:
    lines = file.read().split('\n')


def deduct_translation(patterns: np.ndarray) -> List[Set[str]]:
    """
    deduct the translation of number to mixed up segments
    :param patterns: Array[Set[char]]
    :return: List[Set[str]]
    """
    lengths = np.array([len(p) for p in patterns])  # Length of each sequence
    nr_to_sequence = {
        1: patterns[lengths == 2][0],  # only sequence with length 2
        4: patterns[lengths == 4][0],  # only sequence with length 4
        7: patterns[lengths == 3][0],  # only sequence with length 3
        8: set('abcdefg'),  # only sequence with all 7 segments
    }
    nr_to_sequence[9] = [p for p in patterns[lengths == 6]  # sequence of length 6 in which number 4 is not a subset
                         if nr_to_sequence[4].issubset(p)][0]
    nr_to_sequence[3] = [p for p in patterns[lengths == 5]  # sequence of length 5 in which number 1 is not a subset
                         if nr_to_sequence[1].issubset(p)][0]
    nr_to_sequence[0] = [p for p in patterns[lengths == 6]   # sequence of length 6 that overlaps number 1 but not 4
                         if nr_to_sequence[1].issubset(p)
                         and not nr_to_sequence[4].issubset(p)][0]
    nr_to_sequence[6] = [p for p in patterns[lengths == 6]  # sequence of length 6 that is not 0 or 9 :)
                         if p not in [nr_to_sequence[0], nr_to_sequence[9]]][0]

    c_set: set = nr_to_sequence[1] - nr_to_sequence[6]  # set containing segment c (in the original display)
    f: str = (nr_to_sequence[1] - c_set).pop()  # segment at location of original segment f
    c: str = c_set.pop()  # segment at location of original segment c
    nr_to_sequence[5] = [p for p in patterns[lengths == 5]  # sequence of length 5 that does not include segment c
                         if c not in p][0]
    nr_to_sequence[2] = [p for p in patterns[lengths == 5]  # sequence of length 5 that does not include segment f
                         if f not in p][0]

    return [nr_to_sequence[i] for i in range(10)]  # all sequences at the index of their corresponding number


total = 0
for line in lines:
    digits_pattern, digits_output = line.split('|')  # split 10 patterns and 4 output values
    # Turn both sequences into a list of sets containing the segment characters
    digits_pattern = [set(pat) for pat in digits_pattern.strip().split()]
    digits_output = [set(pat) for pat in digits_output.strip().split()]
    # List of sets of segments in order (index 0 contains the set of segments for number 0 etc.)
    translation = deduct_translation(np.array(digits_pattern))
    total += int(''.join([str(translation.index(p)) for p in digits_output]))

print(total)
