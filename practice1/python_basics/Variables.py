x = 4       # x is int
x = "Sally" # x is now str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#printing variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
