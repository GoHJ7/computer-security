import string
import itertools

gen = open("test_candidate.txt","w")
# Define the set of characters to use for generating words
alphabet = string.ascii_lowercase

# Generate all 3- to 6-letter words
for length in range(3, 7):
    for combination in itertools.product(alphabet, repeat=length):
        word = ''.join(combination)
        gen.write(word + '\n')

gen.close()
