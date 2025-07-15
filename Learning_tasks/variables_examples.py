# Variables
# Variable - a reserved memory location that allows us to store data types and objects

# Number value

x = 5

# Decimal value

y = 3.5

#string value

z = 'Jerome'
print(x, y, z)

# using == seems to run errors

# python is a strongly typed language in that the typing of variables is very important
# if x = 1 and y = '2', x + y will fail

#python is a dynamically typed language in that variable types are checked as the code is executed rather than before the code is executed


print(id(x))

x = 4

print(id(x))

# the id of the variable likely changes because the number value has changed and python operates sequentially

x = 10
y = x

print(id(x))
print(id(y))

# the id values of x and y are the same as they have been made equal to one another

x = 11
print(id(x))
print(id(y))

# the id of y is still the same as the id of the previous x as the order of operations is such that x has changed AFTER y was made equivalent to its previous value

username = 'Nathan Hastings'
age = 24
DOB = "13/05/2001"

print(username, age, DOB)