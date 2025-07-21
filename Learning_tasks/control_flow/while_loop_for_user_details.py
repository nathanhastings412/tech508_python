# SET VARIABLE user_prompt TO TRUE

user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")

    if age.isdigit() and 0 <= int(age) and int(age) <= 117:
        user_prompt = False
    else:
        print("Please enter a number and a valid age")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
        # SET user_prompt TO FALSE
    # ADD ELSE STATEMENT HERE
        # TELL USER THE PROBLEM WITH THEIR INPUT

print(f"Your age is {age}")
