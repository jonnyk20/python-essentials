# Use the Python REPL to evaluate the following expressions

# "hello world"
print("hello world")

# The type of value that "hello world" is
print(type("hello world"))

# 2 plus 2
print(2 + 2)

# 5 - 3 is equal to two
print(5 - 3)

# 4 to the power of 2 is greater than 20
print(4**2)

# 15 is greater or equal to than "hello world"
try:
    print(15 >= "hello world")
except:
    print("An Error has occurred")

# 13 is greater than 100/5 plus 3 or smaller than 2 times 10
print((13 > 100/5) or (13 < 2*10))

# 2 is equal to 2.0
print(2)

# 2 is 2.0
print(1 is 2.0)

# The length of "hello world" is greater than 10 and smaller than 15
print(len("hello world") > 10 and len("hello world") < 15)
