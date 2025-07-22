# functions

# def is_even():
#     number = int(input("Enter a number "))
#     if (number % 2 == 0):
#         return True
#     else:
#         return False
#
# print(is_even())

# for loops
#
# name = "nathan"
#
# for char in name:
#     print(char)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# for num in numbers:
#     if num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     elif num % 3 and num % 5 == 0:
#         print("fizzbuzz")
#     else:
#         print(num)

# While loops

# number = None
#
# while number != 0:
#     number = int(input("Enter a number (0 to stop): "))
#
# print("done!")

# secret_number = 7
# guess = None
#
#
# while secret_number != guess:
#     guess = int(input("Guess the number: "))
#     if guess > secret_number:
#         print("you guessed too high")
#     elif guess < secret_number:
#         print("you guessed too low")
#     else:
#         print("you guessed correctly")

# correct_password = "open123"
# guess = None
#
# while guess != correct_password:
#     guess = input("Enter your password: ")
#     if guess != correct_password:
#         print("Incorrect password, try again.")
#     else:
#         print("access granted")

# Use a for loop to go through the dictionary
#
# Add up all the prices
#
# Print the total cost

# cart = {
#     "apple": 1.50,
#     "banana": 0.80,
#     "bread": 2.25,
#     "milk": 1.75
# }
#
# for fruit in cart:
#     print(f"your total comes to £{cart["apple"] + cart["banana"] + cart["bread"] + cart["milk"]:.2f}")
#
# total = 0
# for price in cart.values():
#     total += price
#
# print(f"Total cost: £{total:.2f}")

# cart = {
#     "apple": {"price": 1.50, "quantity": 4},
#     "banana": {"price": 0.80, "quantity": 6},
#     "bread": {"price": 2.25, "quantity": 1},
#     "milk": {"price": 1.75, "quantity": 2}
# }
#
# total = 0
#
# for item, info in cart.items(): # lets you loop through both the item names and their details
#     price = info["price"]   # pulls price
#     quantity = info["quantity"] # pulls quantity
#     item_total = price * quantity
#     total += item_total
#     print(f"{item}: {quantity} x £{price:.2f} = £{item_total:.2f}")
#
# print(f"Total cost: £{total:.2f}")

# grades = {
#     "Alice": 85,
#     "Bob": 58,
#     "Charlie": 92,
#     "Daisy": 47,
#     "Ethan": 66
# }
#
# total_passes = 0
# total_fails = 0
#
# for name in grades: # loops through the names
#     grade = grades[name] # pulls grades
#     if grade >= 60:
#         total_passes += 1
#         print(f"{name} passed")
#     elif grade < 60:
#         total_fails += 1
#         print(f"{name} failed")
#
# print(f"Total passes: {total_passes}, Total fails: {total_fails}")

# students = {
#     "Alice": {"Math": 75, "English": 82, "Science": 91},
#     "Bob": {"Math": 52, "English": 47, "Science": 65},
#     "Charlie": {"Math": 95, "English": 89, "Science": 93},
#     "Daisy": {"Math": 60, "English": 58, "Science": 55}
# }
#
# total_passes = 0
# total_fails = 0
#
# for name, grade in students.items(): # loop through the names and the grades
#     math = grade["Math"] # pull math grades
#     english = grade["English"] # pull english grades
#     science = grade["Science"] # pull
#     total_grade = (math + english + science)/3
#     if total_grade >= 60:
#         total_passes += 1
#         print(f"{name}: {total_grade:.1f} passed")
#     # print(f"{name}'s grade is {total_grade:.1f}")
#     else:
#         total_fails += 1
#         print(f"{name}: {total_grade:.1f} failed")
#
# print(f"{total_passes} passes, {total_fails} fails")

# sales = {
#     "The Hobbit": 120,
#     "1984": 85,
#     "To Kill a Mockingbird": 90,
#     "The Great Gatsby": 60,
#     "Harry Potter": 150
# }
# total = 0
#
# for book, quantity in sales.items():
#     quantity = int(quantity)
#     total += quantity
# inventory = {
#     "apples": {"price": 0.50, "quantity": 30},
#     "bananas": {"price": 0.30, "quantity": 50},
#     "oranges": {"price": 0.40, "quantity": 40},
#     "grapes": {"price": 1.20, "quantity": 20}
# }
#
# total_price = 0
#
# for item, info in inventory.items():
#     price = info["price"]
#     quantity = info["quantity"]
#     total = price * quantity
#     print(f"{item}: £{total:.2f}")
#     total_price += total
#
# print(total_price)

# students = {
#     "Alice": 82,
#     "Ben": 59,
#     "Clara": 91,
#     "David": 47,
#     "Ella": 75
# }
#
# passes_count = 0
# fails_count = 0
#
# for student in students:
#     grade = students[student]
#     if grade >= 60:
#         print(f"{student} passed")
#         passes_count += 1
#     elif grade < 60:
#         print(f"{student} failed")
#         fails_count += 1
#
# print(f"{passes_count} passed, {fails_count} failed")
#
# balance = 100
#
#
# while balance > 0:
#     print(f"your balance is {balance}.")
#     amount = int(input("How much would you like to withdraw? "))
#
#     if amount == 0:
#         print("transaction cancelled. goodbye!")
#     elif balance < 0:
#         print("transaction failed. please try again.")
#     elif amount > balance:
#         print("insufficient funds. please try again.")
#     else:
#         balance -= amount
#         print(f"£{amount} withdrawn.")

# students = [
#     {"name": "Alice", "scores": [85, 90, 78]},
#     {"name": "Ben", "scores": [56, 64, 70]},
#     {"name": "Clara", "scores": [92, 88, 95]},
#     {"name": "David", "scores": [40, 52, 48]}
# ]
#
# def calculate_average(scores):
#     return sum(scores) / len(scores)
#
# def determine_grade(avg):
#     if avg >= 60:
#         return "pass"
#     else:
#         return "fail"
#
# for student in students:
#     avg = calculate_average(student["scores"])
#     status = determine_grade(avg)
#     print(f"{student['name']} - Average: {avg:.2f} - {status}")

# employees = [
#     {"name": "Alice", "hours_worked": 40, "hourly_rate": 15.0},
#     {"name": "Ben", "hours_worked": 35, "hourly_rate": 12.5},
#     {"name": "Clara", "hours_worked": 50, "hourly_rate": 16.0},
#     {"name": "David", "hours_worked": 30, "hourly_rate": 10.0}
# ]
#
# # def calculate_pay(hours, rate):
# #     return hours * rate
#
# def pay_summary(employee):
#     pay = employee["hours_worked"] * employee["hourly_rate"]
#     return f"{employee["name"]} earned £{pay:.2f} this week."
#
# for employee in employees:
#     print(pay_summary(employee))



# def countdown(start):
#     while start != 0:
#         start -= 1
#         print(f"Time left: {start} seconds")
#     print("time's up!")
# print(countdown(100))

# books = {
#     "Python Basics": {"price": 25.0, "sold": 12},
#     "Data Science 101": {"price": 30.0, "sold": 8},
#     "AI for Beginners": {"price": 20.0, "sold": 15},
#     "Web Dev Guide": {"price": 22.5, "sold": 10}
# }
#
# total_price = 0
#
# for book in books:
#     price = books[book]["price"]
#     sold = books[book]["sold"]
#     total_price += price * sold
#
# print(f"Total sales: £{total_price:.2f} in sales")


# groceries = {
#     "Apples": {"price": 0.50, "sold": 120},
#     "Bananas": {"price": 0.30, "sold": 150},
#     "Carrots": {"price": 0.20, "sold": 200},
#     "Milk": {"price": 1.15, "sold": 75},
#     "Bread": {"price": 1.00, "sold": 60}
# }
#
# total = 0
#
# for item, info in groceries.items():
#     price = groceries[item]["price"]
#     sold = groceries[item]["sold"]
#     total += price * sold
#
# print(f"Total revenue: {total}")

# ticket_sales = {
#     "Adult": {"price": 12.00, "sold": 80},
#     "Child": {"price": 8.00, "sold": 45},
#     "Senior": {"price": 10.00, "sold": 30},
#     "Student": {"price": 9.00, "sold": 20}
# }
# total = 0
#
# for ticket, info in ticket_sales.items():
#     price = info["price"]
#     sold = info["sold"]
#     total += price * sold
#
# print(f"Total: {total}")
#
# password = "letmein"
# guess = None
#
# while guess != password:
#     input("enter password: ")
#     if guess != password:
#         print("access denied. try again")
#     else:
#         print("access granted")

# secret_number = 17
# guess = None
#
# while guess != secret_number:
#     guess = int(input("Guess the secret number: "))
#     if guess < secret_number:
#         print("Your guess is too low")
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print("You guessed correctly")




# def calculate(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         return num1 / num2
#     else:
#         print("Invalid operator")
#
#
# print(int(input(f"Enter first number: ")))
# print(int(input(f"Enter second number: ")))
# print(int(input(f"Enter operator: ")))
# print("Result")

# def greet(name):
#     print(f'Hello {name}!')
#
# greet("Nathan")

def rectangle_area(width, height):
    return width * height
    if isnegative(width) or isnegative(height):
        return "invalid dimensions"
    else:
        print(rectangle_area(width, height))

rectangle_area(5, 10)

