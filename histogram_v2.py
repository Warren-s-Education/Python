from os import strerror
from operator import itemgetter


# initialise data structure for storing letter counts
first_letter = 'a'
last_letter = 'z'
letter_counts = {
    chr(codepoint): 0
    for codepoint in range(ord(first_letter), ord(last_letter) + 1)
}


# After opening ``file_name``, try to count all occurences of the letters in
# the dictionary ``letter_counts``.
try:
    file_name = 'test.txt'
    read_stream = open(file_name, 'rt')
    # Iterates through every character in the read_stream.
    for line in read_stream:
        for character in line:
            # If a character is alphabetic, we increment our count of its number of
            # occurences by 1. Since our count is not case-sensitive, incrementation is
            # achieved by adding 1 to the value of the key ``character.lower()`` in
            # ``letter_counts``.
            if character.isalpha():
                letter_counts[character.lower()] += 1
    read_stream.close()
except IOError as error:
    print('Reading error:', strerror(error.errno))
    exit(error.errno)

# Sort the dictionary ``letter_counts`` by decreasing value.
descending_letter_counts = dict(
    sorted(
        letter_counts.items(),
        key=itemgetter(1),
        reverse=True
    )
)

# Try to write the non-zero letter counts to a file in descending order
try:
    destination_file = file_name.replace('.txt', '.hist')
    write_stream = open(destination_file, 'wt')
    for letter, count in descending_letter_counts.items():
        if count > 0:
            write_stream.write(f"{letter} -> {count}\n")
    write_stream.close()
except IOError as error:
    print('Destination file error:', strerror(error.errno))
    exit(error.errno)

# print('Execution of ``histogram_v2.py`` successful.')
