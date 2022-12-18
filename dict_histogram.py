from string import ascii_lowercase
from os import strerror

# Initialise 26 counters for the Latin alphabelt.
letter_counts = {character:0 for character in ascii_lowercase}

try:
    stream = open('test.txt', 'rt')
    for line in stream:
        for character in line:
            if character.isalpha():
                letter_counts[character.lower()] += 1
    stream.close()
except IOError as e:
    print(strerror(e.errno))

for letter, count in letter_counts.items():
    if count > 0:
        print(f"{letter} -> {count}")