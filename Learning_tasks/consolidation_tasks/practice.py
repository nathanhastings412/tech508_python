


# age_int = int(input("what is your age? "))
# name_str = input("what is your name? ")
# print(f"OMG {name_str}, you are {age_int} years old so you were born in {2025-(age_int)}")
#
# total_hours = age_int * 365 * 24


#python string equality - checking if a string is equal to certain things
# name = "Alice"
#
# if name == "Alice":
#     print("Hello, Alice!")  # This will run
#
#
# colour = "blue"
# if colour in ["red","blue","green"]:
#     print("that's a valid colour")
#
# word = "Python"
#
# if word.lower() == "python":
#     print("Match!")  # True even if the original was "PYTHON"
#
# if name != "Bob":
#     print("You're not Bob!")
#
# name = "Alice"
# is_alice = name == "Alice"
#
# print(is_alice)  # Output: True
#
# def is_valid_user(user):
#     return user.lower() == "alice"
#
# print(is_valid_user("A"))




# simple boolean expression
# claculator

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = input("Enter operator: ")
#
# def add(num1, num2):
#     return num1 + num2
# def subtract(num1, num2):
#     return num1 - num2
# def multiply(num1, num2):
#     return num1 * num2
# def divide(num1, num2):
#     return num1 / num2
#
# if operator == "+":
#     print(add(num1, num2))
# elif operator == "-":
#     print(subtract(num1, num2))
# elif operator == "*":
#     print(multiply(num1, num2))
# elif operator == "/":
#     print(divide(num1, num2))
# else:
#     print("enter a valid operator")



# python shopping cart list
#
# expenses = {
#     "groceries": 45.50,
#     "transport": 15.00,
#     "entertainment": 22.75,
#     "coffee": 8.25,
#     "utilities": 60.00
# }
#
# total = 0
# for item in expenses:
#     total += expenses[item]
#
# print(f"Total: £{total:.2f}")
# expenses = {
#     "groceries": 45.50,
#     "transport": 15.00,
#     "entertainment": 22.75,
#     "coffee": 8.25,
#     "utilities": 60.00
# }
#
# def calculate_total():
#     total = 0
#     for expense in expenses:
#         expense = expenses[expense]
#         total += expense
#     print(total)
#
# calculate_total()
#
# def sum_list(numbers):
#     return sum(numbers)
# print(sum_list([6,3,5,6,7]))

# def is_weekend(day):
#     weekend_days = ["saturday", "sunday"]
#     if day in weekend_days:
#         return True
#     else:
#         return False
#
# print(is_weekend("sunday"))
# print(is_weekend("saturday"))
# print(is_weekend("monday"))

# def is_even(num):
# #     return
#
# numbers = [1, 4, 5, 8, 10, 3]
# even_numbers = (numbers.iseven())
#
# print(sum(even_numbers))
#
# students = {
#     "Emma": {"math": 90, "english": 85},
#     "Liam": {"math": 78, "english": 92}
# }
#
# for student, score in students:
#     math_score = students[student]["math"]
#     english_score = students[student]["english"]
#     print(f"Student: {student}, Score: {math_score}, English: {english_score}")

# def char_frequency(s):
#     freq = {}
#     for char in s.lower():
#         if char != " ":
#             freq[char] = freq.get(char, 0) + 1
#     return freq
#
# print(char_frequency("Hello World"))
#
# def remove_outliers(numbers, lower, upper):
#     return [num for num in numbers if lower <= num <= upper]
#
# print(remove_outliers([3, 7, 2, 9, 15, 1], 3, 10))