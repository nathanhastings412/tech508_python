# = is used to create a variable - it is assignment
# == is equal to - it is compariso

# x = 5
# y = "5"

# print(x == y) - False
# print(x == int(y)) - True
# swap the values
# a = 10
# b = 20
# a, b = b, a

# number = None
#
# while number != 0:
#     number = int(input("Enter a number: "))
#     if number > 0:
#         print("positive")
#     elif number < 0:
#         print("negative")
#     else:
#         print("zero")

# for i in range(1, 6):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# for loops loop through every item in an iterable
# while loops loop while a condition is active

# a list is made between [,] and can be ammended
# a tuple cannot be ammended and is made with (,)

# my_list[-1]

# nums.pop(2)
# also nums.remove(3)

# def greet(name):
#     print(f"Hello {name}")
#
# greet("John")

# parameter is the variable in the function definition (e.g. name in def greet(name))
# argument is the actual value passed (e.g. "John")
# return sends a value back from the function to the caller

# def analyze_scores(scores):
#     if not scores:
#         return {"average": 0, "highest": None, "passed": False}
#     average = round(sum(scores) / len(scores), 2)
#     highest = max(scores)
#     pass_count = 0
#     for score in scores:
#         if score >= 50:
#             pass_count += 1
#     passed = pass_count > (len(scores) / 2)
#     return {"average": average, "highest": highest, "passed": passed}
#
#
#
# print(analyze_scores([75, 62, 48, 90, 55,30]))

# def summarise_expenses(expenses):
#     if not expenses:
#         return {"total": 0, "high_expenses": 0, "flagged": False}
#     total = round(sum(expenses, 2))
#     high_expenses = expenses[expenses > 100]
#     for flagged in high_expenses:
#         if flagged > 500:
#             return True
#         else:
#             return False
#
#
# expenses = [25.50, 120.75, 78.40, 560.00, 32.10, 15.99]
# print(summarise_expenses(expenses))

# Python Question Approach

# identify the input and expected output
# look for keywords
# are there any edge cases to consider (e.g. empty lists, zeros, negative numbers)
# rephrase the problem in your own words
# sum

# def is_teenager(age):
#     if age >= 13 and age <=19:
#         return True
#     else:
#         return False
#
# print(is_teenager(20))
#
# def can_borrow_book(age, has_library_card):
#     if age >= 12 and has_library_card:
#         return True
#     elif age < 12 and has_library_card:
#         return True
#     else:
#         return False
#
# print(can_borrow_book(20, True))
# def can_enter_lab(is_employee, has_badge, is_visitor, has_escort):
#     if is_employee and has_badge:
#         return True
#     elif is_visitor and has_escort:
#         return True
#     else:
#         return False
#
# print(can_enter_lab(True, True, True, True))
# print(can_enter_lab(True, True, True, False))
# print(can_enter_lab(True, False, False, True))

# input_list = [
#     "apple", "banana", "None", "orange", "plastic", "", "Apple", "BANANA", "grape", "pear", "Pear"
# ]
#
# def process_fruits(fruit_list):
#     fruit_list.lower().remove("None", "plastic", "")
#     for fruit in fruit_list:
#         print(f"{fruit}: {fruit_list.count(fruit)}")
#     return fruit_list
#
# print(process_fruits(input_list))

# cart = {
#     "apple": {"price": 0.99, "quantity": 3},
#     "banana": {"price": 0.59, "quantity": 5},
#     "milk": {"price": 2.49, "quantity": 2}
# }
#
#
# def calculate_total(cart):
#     total = 0
#     for item, info in cart.items():
#         price = info["price"]
#         quantity = info["quantity"]
#         total += price * quantity
#     print(f"Total: £{total:.2f}")
#
# print(calculate_total(cart))

# import random
#
#
#
# def number_guess_game():
#     random_number = random.randint(1, 10)
#     guess = int(input("Enter a number (1-10): "))
#     guess_count = 0
#     while True:
#         if guess > random_number:
#             guess_count += 1
#             print("too high")
#             continue
#         elif guess < random_number:
#             guess_count += 1
#             print("too low")
#             continue
#         else:
#             print(f"You guessed the number in {guess_count} guesses")
#             break
#
# print(number_guess_game())

def calculate(num1,num2,operator):
