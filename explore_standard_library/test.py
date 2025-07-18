#import this


# random module
# import random
#
# print(random.random())
# randnum = random.randint(1, 10)
# print(randnum)


# math module
# import math
#
# num_float = 23.66
#
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)
# # gives us remainder of the 2 values
# # 5 can't go into 1, so the remainder is 1
# print(f"Remainder from 1/5: {math.remainder(1, 5)}")


# os module

# import os
#
# # returns our current working directory
#
# working_directory = os.getcwd()
# print(f"Current working directory: {working_directory}")
#
# username = os.environ.get('USERNAME') or os.environ.get('USER')
# print(f"The current user is: {username}")
#
# cpu_cores = os.cpu_count()
# print(f'Total CPU cores: {cpu_cores}')
#
# # change directory - must exist
# # os.chdir("<folder_name>")
#
# # make a new directory
# os.mkdir("created_by_python")

# import sys module

# import sys
# # gives us the current paths important to the Python interpreter
# print(f"Current path: {sys.path}")
# print(sys.version)

# import datetime module

# import datetime
#
# # gives us today's date
# print(f"Today's date: {datetime.date.today()}")
#
# #gives us todays date and time
# print(f"Today's date: {datetime.datetime.now()}")

# import builtin functions

# import builtins
#
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# import requests
#
# request_bbc = requests.get("https://www.bbc.co.uk/")
#
# print(request_bbc.status_code)
#
# print(request_bbc.content)