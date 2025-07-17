shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[0]) # prints first item
print(shopping_list[-1]) # prints last item
shopping_list[1] = "rice" # changes second item to rice
print(shopping_list)
shopping_list.append ("carrots") # adds carrots to the list
print(shopping_list)
shopping_list.extend (["toffee", "coffee"]) # extends the list
print(shopping_list)
shopping_list.remove ("bananas") # remove item from list
print(shopping_list)
shopping_list.pop() # if you don't specify which item, it will remove the last item
print(shopping_list) # remove last item from list
