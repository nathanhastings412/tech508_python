# Make a function called "calc_percent"
# The function should convert the score (into) into a percent and return the percent
# Integer received by the function is a number between 0-20 (a score out of 20)

def calc_percent(score):
    # Converts a score out of 20 into a percentage
    return (score / 20) * 100

while True:
    user_input = input("Input a score out of 20: ")

    if user_input.isdigit():
        score = int(user_input)
        if 0 <= score <= 20:
            break  # Valid input, exit the loop
        else:
            print("Enter a score from 0-20 in digits")
    else:
        print("Enter a score from 0-20 in digits")

# Convert to percentage
percent = calc_percent(score)

# Print the result rounded to nearest whole number
print(f"Score converted to a percentage: {round(percent)}%")
