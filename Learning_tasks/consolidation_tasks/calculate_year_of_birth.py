age_int = input("Enter your age: ")
name_str = input("Enter your name: ")

current_year = 2025
year = current_year - int(age_int)

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year}")

birth_year = int(input("Enter your birth year: "))

total_days = (current_year - birth_year) * 365
total_hours = total_days * 24

print(total_hours)