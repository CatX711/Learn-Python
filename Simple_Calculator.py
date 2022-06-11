# If you thought that making a calculator in Python is probably extremely hard, you're wrong.
# You have all the tools at your disposal to make one. A simple calculator that adds up the two numbers that you input can be made in 2 minutes or less.
# Let's give it a try.
# First, create a "number1" variable, and a "number2" variable, that both equal some input:

number1 = input("Enter your first number: ")
number2 = input("Enter your second number: ")

# (You can have anything inside the input("") that you want.)

# Now, add int and brackets around the two inputs for the two variables, like this:

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

# This will convert whatever number you type from string into an integer.
# After that, type "print" and inside the brackets, number1 + number 2

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
print(number1 + number2)

# Then you can polish it off with some beginning text, and end text.

print("Welcome, to the simple calculator! This calculator adds two numbers up together, and gives you your result.")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
print("Your number is: ", number1 + number2)
