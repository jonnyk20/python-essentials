# import the following modules: random.shuffle, os.system, csv.reader
from random import shuffle
from os import system
from csv import reader

# write a method to clear the terminal


def promptToClear():
    print("--------Press any key to continue--------")
    input()
    system("clear")


# create a list to store majors
# import majors into list
majorsTXT = open('../data/majors.txt', 'r')
majors = majorsTXT.read().split('\n')
majorsTXT.close()

# create a list to store names
# import names into that list
namesCSV = open('../data/names.csv', 'r')
names = list(reader(namesCSV))
namesCSV.close()

# shuffle lists
shuffle(majors)
shuffle(names)

# create a variable to store the number of people you'd like to try to remembers

# generate list of profiles
# for majors
profiles = []
for major in majors[:3]:
    profiles.append({
        "major": major,
        "name": names.pop()[1]
    })

    # Print that list one by one in the terminal
    # Hi, I'm ___ and I study ____
    # Prompt the user to press any key to meet the next person
    # Clear the terminal when they do
for profile in profiles:
    print(f'Hi, I\'m {profile["name"]} and I study {profile["major"]}')
    promptToClear()

# set up a variable to track total profiles
# set up a variable to track total answers
# set up a variable to track total correct answers
# using the above, set up a variable to calculate incorrect answers
total = len(profiles)
answers = 0
correct = 0
incorrect = answers - correct

# shuffle the list of profiles
shuffle(profiles)

# Loop throught profiles and do as follows
for profile in profiles:
    # ask the user about who has a particular major
    print(f'Who studies {profile["major"]}')

    # get their answer through input
    answer = input()
    # add 1 to the number of answers
    answers += 1
    # compare their answer to the actual value (think about casing as well, if you can)
    if (answer.lower() == profile["name"].lower()):
        # if it's correct,
        # Let the user know their answer was correct
        # increment the correct counter
        print("Correct!")
        correct += 1
    else:
        # if not
        # Let the user know their answer was NOT correct
        # Show them the correct answer
        print("Ha! You thought!")
        print(f'The correct answer is: {profile["name"]}')

    # print results so far "Score: x/y"
    print(f'Score: {correct}/{answers}')
    # Calculate the ramining questions and save the value to a variable
    remaining = total - answers
    # Check if that value is greater than 0
    if (remaining):
        print(f'{remaining} questions remaining')
        # If so,
        # let then know how many are remaining
        # Prompt the user to press any key to see the next question
        # Clear the terminal when they do
        promptToClear()
    else:
        # if not,
        # Thank them for playing
        print('Thank you for playing!')


# Bonus Step
# There will likely be a lot of repeated code in the first version of this program
# See how you can optimize it by abstrating some of the steps into resulable methods
