import sys

print(sys.version)

print("hello, world!")

#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
  print("Five is greater than two!")

x = 5
y = "Hello, World!"

print(x)
print(y)

"""
This is a comment
written in
more than just one line
"""

x = 5
y = "John"
print(type(x))
print(type(y))

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print(x, y, z)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)