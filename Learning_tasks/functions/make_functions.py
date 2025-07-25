# # Task 1
# import string
# from time import process_time_ns
#
#
# def print_something():                # define function
#     print("this function is running") # this is the code
#
# print_something()                     # call function
#
# # Task 2
#
# # argument is like a prerequisite for the function to work
#
# def print_something(string):
#     print(string)
#
# print_something("This is a string")
# print_something("This is another string")
#
# # Task 3
#
# def greet(susan):
#     print("hello, my name is " + susan)
#
# greet("susan")
#
# # Task 4
#
# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(1, 3))
# addition(2, 2)
#
# # return does not yet action anything
#
# # Task 5
#
# def addition(int1 = 2,int2 = 2):
#     return int1 + int2
#
# print(addition())
# print(addition(4,4))
#
# # the default integer values are 2 but can be defined as different values
#
# # Task 6
#
# def print_every_number(*numbers):
#     print(numbers)
#     print(type(numbers))
#     for number in numbers:
#         print(number)
#
# print_every_number(1,2,3,4,5,6)
#
# # * allows you to put in a tuple as opposed to an integer (multiple numbers)

# Task 7

# def greet(number: str):
#     print("hello, my name is " + (number))
#
# greet(24601)

# adding : <data_type> to the argument implies which data type should be called

# Task 8

# def division(num1: int = 2, num2: int = 5) -> float:
#     return num1/num2
# a = 4
# b = 6
# print(division(a,b))

# you can put static values as variables into your functions

# Task 9

# function name should be relevant/descriptive (maybe a verb)
# a function should have a single function
# a doc string is a multi line string which explains what the code does
# a doc string often goes at the top of a function

# def calculate_area(length, width):
#     """
#     Calculates the area of a rectangle.
#
#     Args:
#         length (float): The length of the rectangle.
#         width (float): The width of the rectangle.
#
#     Returns:
#         float: The calculated area of the rectangle.
#     """
#     return length * width


# # You can access the docstring using the __doc__ attribute
# print(calculate_area.__doc__)
#
# # Or using the help() function
# help(calculate_area)