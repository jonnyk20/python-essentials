# Create a 'user' dictionary with your name, age, and a list your favorite foods
user = {
    "name": "John",
    "age": 76,
    "foods": ["chips", "pizza", "burgers"]
}

# Using that dictionary print out our age
print(user["age"])

# Using that dictionary, print out your second favorite food
print(user["foods"][0])

# Create a list with three more people, ask the people aroudn you for their info
others = [
    {
        "name": "Mary",
        "age": 27,
        "foods": ["ribs", "lobster", "apples"]
    },
    {
        "name": "Tom",
        "age": 32,
        "foods": ["broccoli", "salmon", "pasta"]
    },
    {
        "name": "Adam",
        "age": 24,
        "foods": ["chicken", "bananas", "pie"]
    }
]


# loop though each of them and print out the following phrase
# Hi, I'm ___, in 20 years, I will be __ years old, living with my mother, spending all day eating __fav food_'
# Be careful with the quotation marks!
# Bonus: Change the phrase to lsirt all of the foods, putting "and" jsut before the last one
for other in others:
    print(f'Hi, I\'m {other["name"]}, in 20 years, I will be {other["age"] + 20} years old, living with my mother, spending all day eating {other["foods"][0]}')

for other in others:
    upTolast = ", ".join(other["foods"][:-1])
    print(f'Hi, I\'m {other["name"]}, in 20 years, I will be {other["age"] + 20} years old, living with my mother, spending all day eating {upTolast}, and {other["foods"][-1]}')
