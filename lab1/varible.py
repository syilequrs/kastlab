x = 23
y = "korobka"
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

x = "5"
y = "banan"
print(type(x))
print(type(y)) #<class 'str'>
               #<class 'str'>

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
2myvar = "J"
my-var = "o"
my var = "hn"
these are illegal!!!!
"""
x, y, z = "sd", "cd", "bd"
print(x)
print(y)
print(z)

x = y = z = "banan"
print(x)
print(y)
print(z)

leg = ["first", "second", "variable"]
x, y, z = leg
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)
x = "Python"
y = "is "
z = "awesome"
print(x, y, z)
x = "Python "
y = "isn't "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
"""
x = 5
y = "John"
print(x + y)    you cant add two different vabilelsldbses 
"""
x = 5
y = "John"
print(x, y)

x = "ok"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) #local >>>>>>>>>>>>>> global

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #global becomes