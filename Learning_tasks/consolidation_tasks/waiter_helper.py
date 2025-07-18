# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user

print(f"Welcome")

# Print a list of starters

starters = {"gyoza" : 4, "garlic bread" : 5, "chicken satay skewers" : 3}
print(starters)

# Take an input for the user for their starter

starter = input("what starter can I get for you? ")

# Print a list of mains

mains = {"lasagne" : 10, "mac n' cheese" : 11, "beef rigatoni" : 12}
print(mains)

# Take an input for the user for their main course

main = input("and what would you like for your main? ")

# Print a list of desserts

desserts = {"ice cream" : 4 , "sticky toffee pudding" : 5, "lemon sorbet" : 3}
print(desserts)

# Take an input for the user for their dessert

dessert = input("and what would you like for your desserts? ")

# Print all the user's choices

print(f"so that would be the {starter}, the {main}, and {dessert}")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

customer_order_list = [starter, main, dessert]
print(customer_order_list)

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

customer_bill = (starters[starter] + mains[main] + desserts[dessert])
print(f"Your bill comes to £{customer_bill}")
#
# prices = {
#     "gyoza" : 3,
#     "garlic bread" : 4,
#     "chicken satay skewers": 5,
#     "beef rigatoni": 10,
#     "lasagne" : 11,
#     "mac n' cheese" : 12,
#     "ice cream" : 4,
#     "sticky toffee pudding" : 5,
#     "lemon sorbet" : 3,
# }



# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
