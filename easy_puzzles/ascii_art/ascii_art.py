import sys
import math

def main(l: int, h: int, t: str, provided_alphabet: list) -> list:
    ALPHABET_LENGTH = 27

    alphabet = {}
    letter_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, '?': 26}
    to_print = []

    for i in range(h):
        row = provided_alphabet[i]
        for j in range(ALPHABET_LENGTH):
            if (i == 0):
                alphabet[j] = []
            alphabet[j].append(row[j * l:(j * l) + l])

    for index, letter in enumerate(t):
        if (letter.isalpha()):
            digit_map = letter_mapping[letter.upper()]
        else:
            digit_map = letter_mapping['?']
        for sub_index, line in enumerate(alphabet[digit_map]):
            if (index == 0):
                to_print.append('')
            to_print[sub_index] += line

    return to_print

# TO PRINT TO CONSOLE

# provided_alphabet = []

# l = int(input())
# h = int(input())
# t = input()
# for i in range(h):
#     provided_alphabet.append(input())

# result = main(l, h, t, provided_alphabet)
# for line in result:
#     print(line)