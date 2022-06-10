# What is an integer in Python? An integer is basically a number, and a string is text. When you type a number into a variable, the language assumes that it is a string,
# but to not have this, we have to convert the input into an integer.
# What you do is you type "int" and in open and closed brackets, type your variable that equals an input.
# Your program would look like this:

marmalade = input("Type a number: ")
int(input())

# This converts the input, for example, 5, from string, which is what the computer assumes it is, into an interger.
# Then you can get the program to print the input x2. To do this, with your old code, write, "print(int(input()) * 2)" (times in Python is an asteric) 

marmalade = input("Type a number: ")
int(input())
print(int(input()) * 2)

# Your result should be the program asking you for a number, and then taking that number, realising it is a number, and not text, and multiplying it by two.

# Type a number: 7
# 14

# We can expand upon this, by adding text into our final print line.
# In Python, different things can be seperated by a comma, so if you wanted to add text to a print function that repeats your name, it wuld look like this:

name = input("Type a name: ")
print("Your name is", input(), "!")

# You should get this:
# Type a name: Ronald
# Your name is Ronald!

# Now do this to your code, eg:

print("Your number multiplied by two is: ", marmalade)

# You should get this as your response:
# Type a number: 
