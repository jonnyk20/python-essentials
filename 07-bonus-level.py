import random;

# Beginner mode
surnamesRaw = open('./name-lists/census-dist-2500-last.txt', 'r').read()
surnamesRaw = surnamesRaw.split('\n')
surnames = []
for surname in surnamesRaw:
    surnames.append(surname.split(' ')[0])

# Pro mode
femaleNames = [name.split(' ')[0] for name in open('./name-lists/census-dist-female-first.txt').read().split('\n')]
maleNames = [name.split(' ')[0] for name in open('./name-lists/census-dist-male-first.txt').read().split('\n')]

randomNumber = random.randint(0, 101)


"""
We're given 3 lists:
    - List of surnames names
    - List of female names
    - List of male names

This is US census data from 1990. You can read more here: https://deron.meranda.us/data/

We're also given an example of how to generate a random number between 1 and 100.

See if you can work out how to use these tools, plus what you've already learned,
to generate a random name when the script runs.

Enhancements:
    - Randomly choose between the male/female name lists
    - Generate one male name and one female name each time the script is run
    - Make the names "Title Case" instead of "UPPER CASE"
    - Generate 5 male names and 5 female names
    - Calculate how common the generated full name is (Hint: There is more data
        in the textfile than what winds up in 'femaleNames' and 'maleNames')
"""
