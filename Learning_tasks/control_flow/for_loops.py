list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}
}

# Task 1

# for num in list_data:
#     print(num * 2)

# Task 2

# for data in embedded_lists:
#     print(data)

# Task 3

# for data in embedded_lists:   # outer loop
#     print(data)
#     for item in data:         # inner loop
#         print(item)

# Task 4

# for num in dict_data:
#     print(num)

# Task 5

# for item in dict_data.values():
#     print(item)

# Task 6

# for value in dict_data.values():
#     for nested_value in value.values():
#         print(nested_value)

# Task 7

# for value in dict_data.values():
#     for nested_value in value:
#         if nested_value == "money":
#             print(value[nested_value])

# for item in dict_data.values():
#     print(item["money"])

# items = ["apple", "banana", "cherry"]
#
# for item in items:
#     print(item)
#     for character in item:
#         print(character)

# Task 8

# for num in list_data:
#     if num < 3:
#         print('less than 3')
#     elif num == 3:
#         print('I found three')
#     else:
#         print('greater than 3')
