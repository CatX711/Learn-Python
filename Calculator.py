# Things are getting real now. In this, you will make the calculator divide, subtract, add and multiply. And you get to choose which one you want it to do.

# Start off by creating a variable with a name called "selection", which equals and input.

selection = input("Select what to do (add/multiply/divide/subtract")

# Then type if selection.lower() == "add":
# There's a lot to unpack there, so I'll go over it now. If, elif, and else, make the computer do something if it is true or false.
# e.g:

if 3 > 5:
  print("Hello")
elif 5 > 3:
  print("World")
  
# The computer will always print "World", but if you say, three is greater than 5, things are different:

3 > 5
if  3 > 5:
  print("Hello")
elif 5 > 3:
  print("World")

# You'll probably notice that python throws all logic out of the window and prints "Hello", except, it doesn't. You tell the program that three is greater than five, so
# going off of what you said, prints "Hello".

# .lower() is easy to understand. Basically, it converts whatever you write into lowercase, so if your answer always had to be in lowercase, you would just type
# .lower at the end of your variable name.
# e.g:

food = input("What do you want for breakfast today? (bacon/sausages)")
if food.lower() == "bacon":
  print("Tasty!")
elif food.lower() == "sausages":
  print("Tasty!")
else:
  print("That is not a valid option.")
  
# That is where else comes in. What ese does is checks if the user typed "bacon", or "sausages", and, if it typed something else like "black pudding"  
  
             

  
  
                  
                  
