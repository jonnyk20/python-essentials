# Make a list of your favorite animals and store it in a variable
animals = ["dog", "cat", "rabbit"]

# Print out the third item on that list
print(animals[2])

# Print out how many items are in that list, (don't write the number direcly)
print(len(animals))

# One by one, print out the phrase "I have a ___." which each of yur animals
for animal in animals:
    print(f"I have a {animal}")

# Create a list of different kinds of food (use plural)
foods = ["chips", "pizza", "burgers"]


# For each of your animals, print out "My __ is eating ___." for each of the food types.
# There should be a totla of (number of aninals x number of foods) pheases being printed
for animal in animals:
    for food in foods:
        print(f"My {animal} is eating {food}.")
