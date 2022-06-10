# What is an integer in Python? An integer is basically a number, and a string is text. When you type a number into a variable, the language assumes that it is a string,
# but to not have this, we have to convert the input into an integer.
# What you do is you type "int" and in open and closed brackets, type input(your text).
# Your program would look like this:

marmalade = int(input("Type a number: "))

# This converts the input, for example, 5, from string, which is what the computer assumes it is, into an interger.
# Then you can get the program to print the input x2. To do this, with your old code, write, "print(int(input()) * 2)" (times in Python is an asteric) 

marmalade = int(input("Type a number: "))
print(int(input()) * 2)

# Your result should be the program asking you for a number, and then taking that number, realising it is a number, and not text, and multiplying it by two.

# Type a number: 7
# 14

# We can expand upon this, by adding text into our final print line.
# In Python, different things can be seperated by a comma, so if you wanted to add text to a print function that repeats your name, it wuld look like this:

name = int(input("Type a name: "))
print("Your name is", input(), "!")

# You should get this:
# Type a name: Ronald
# Your name is Ronald!

# Now do this to your code, eg:

print("Your number multiplied by two is: ", marmalade * 2)

# You should get this as your response:
# Type a number: 22
# Your number multiplied by two is: 44

# Full code:

marmalade = int(input("Type a number: "))
print("Your number multiplied by two is:", marmalade * 2)
