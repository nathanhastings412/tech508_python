# function = block of reusable code

# def
# function name
# () parameters
# code
# call function
# () in the call is the argument

# return # statement used to end a function and send a result back to the caller

# make a calculator

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = input("Enter operator: ")
#
#
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
#
#
# if z == "+":
#     print(add(x, y))
# elif z == "-":
#     print(subtract(x, y))
# elif z == "*":
#     print(multiply(x, y))
# elif z == "/":
#     print(divide(x, y))
# else:
#     print("Invalid operator")

# 1

# def add(a,b):
#     return a+b

# 2 return ends the function and returns statement back to the caller whilst print just prints

# 3 "Hello"

# 4

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(2))

# 5 11

# 6

# def count_vowels(s):
#     vowels = ["a","e","i","o","u"]
#
#     if vowels in s:
#         print(vowels)
#
#     # for letter in s:
#     #     if letter in vowels:
#     #         print(letter)
#
# count_vowels("How many vowels are in this string?")

# 7
#
# def factorial(n):
#     return 1 if n==0 else n*factorial(n-1)
#
# print(factorial(5))

# 8
#
# def max_of_three(a,b,c):
#     return max(a,b,c)
#
# print(max_of_three(5,5,6))
#
# # 9 returns the value of input s times input n
#
# # 10
#
# def reverse_list(lst):
#     return lst[::-1]
#
# # 11
#
# print(reverse_list([1,2,3,4,5]))
#
# def greet(name="friend"):
#     return f"Hello {name}"
#
# print(greet())

# 12 it will add 1 and 2 to my_list

# 13
#
# def fizz_buzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Buzz"
#     else:
#         return n
# print(fizz_buzz(5))
#
# # 14
#
# # 15
#
# def stats(nums):
#     print(nums.max(), nums.min(), nums.avg())
#

# is_hot = True
# is_cold = False
#
# print(not is_hot)         # False
# print(is_hot and is_cold) # False
# print(is_hot or is_cold)  # True
