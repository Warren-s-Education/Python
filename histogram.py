from os import strerror

# The ith index of the sorted 'letters' array stores the count for the ith letter.
letters = [0] * 26
starting_letter = 'a'


# The code point of 'starting_letter' is calculated; by subtracting this code point from the code point of any letter to be counted, the correct index of 'letters' is located. This works because 'letters' is sorted. 
starting_code_point = ord(starting_letter)

try:
    # get file name then try to open the file
    # source_name = input("enter file name")
    stream = open('test.txt', 'rt')
    # try to read characters one at a time and update letter count
    while letter_to_be_counted := stream.read(1).lower():
        index = ord(letter_to_be_counted) - starting_code_point
        letters[index] += 1
except IOError as e:
    print('processing error:', strerror(e.errno))
    exit(e.errno)
except Exception as e:
    print(e.``)
    exit(1)


for index in range(len(letters)):
    letter = chr(starting_code_point + index)
    print(f"{letter} -> {letters[index]}")