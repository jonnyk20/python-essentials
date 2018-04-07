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

randomIndexFemale = random.randint(0, len(femaleNames))
randomIndexMale = random.randint(0, len(maleNames))
randomIndexSurname = random.randint(0, len(surnames))

print(femaleNames[randomIndexFemale] + ' ' + surnames[randomIndexSurname])
print(maleNames[randomIndexMale] + ' ' + surnames[randomIndexSurname])
