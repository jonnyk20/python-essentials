greeting = "Hello" # Try to notice where we override this later.

# Hey this is the first time we care about indentation!
objects = [
    "World",
    "Gang",
    "Y'all",
    "Everybody",
    "Everyone",
    # You can put a comment here, so that's neat.
    "😁",
    "Sam",
    "Anita",
    "Ralph",
    "Mario",
]


# Bad plan. What if our list has 28,000 items in it?
print(greeting + " " + objects[0]) # 0 is the first in every list
print(greeting + " " + objects[1])
print(greeting + " " + objects[2])
print(greeting + " " + objects[3])
print(greeting + " " + objects[4])
print(greeting + " " + objects[5])
print(greeting + " " + objects[6])
print(greeting + " " + objects[7])
# Ugh. This is laborious.

print("\nDon't do that ☝️")
print("--------")
print("Do this 👇\n")

for _object in objects:
    print(greeting + " " + _object)

# Nested loops

print("\n--------\n")

greetings = [
    "Hello",
    "Hey there,",
    "Howdy",
    "你好",
    "👋"
]

for greeting in greetings:
    for _object in objects:
        print(greeting + " " + _object)

print("\n--------\n")

tails = [
    "How's it going?",
    "I didn't see you there.",
    "You wanna get a sandwich or something?",
    "🎉🎮👾🐳👌"
]


for greeting in greetings:
    for _object in objects:
        for tail in tails:
            print(greeting + " " + _object + "! " + tail)
