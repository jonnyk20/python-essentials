# use the followgin variable for the rest of the exercises

name = "John"  # Your name
city = "Detroit"  # Your home city
major = "Finance"  # Your major


# 1: Concatenation
# by combinng strings, print out "Hi, I'm ___, I'm from __ and I study __.'"
print("Hi, I'm " + name + ", I'm from " + city + " and I study " + major + ".")

# 2: Replace
# create a varable called greeting
# Assign to it a greeting with placeholder keywords like "Hi my name is [name] and I live in [city]"
# replace the name variable and print the greeting
# replace thecity variable and print the greeting
greeting = "Hi, I'm [name], I'm from [city] and I study [major]."
greetingWithdata = greeting.replace("[name]", name) \
    .replace("[city]", city) \
    .replace("[major]", major)
print(greetingWithdata)


# 2: Sring Formatting
# In one line of code, print "Hi my name is __ and I live in __."
print("Hi, I'm {}, I'm from {}, and I study {}".format(name, city, major))

# Try it again with the format intputs in a different order
print("Hi, I'm {a}, I'm from {b}, and I study {c}".format(
    b=city, c=major, a=name))

# Try it again with literal string interpolation.
print(f"Hi, I'm {name}, I'm from {city}, and I study {major}")
