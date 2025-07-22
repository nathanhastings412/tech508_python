# Python notes

## code

to do
- finish this document
- learn basic parameters
- consolidate KNOWLEDGE from this last week
- consolidate PYTHON from last week
- try to prepare for interview style questions
- understand using the terminal
- revisit APIs
- practice functions and loops

tools
- W3 schools
- python libraries
- youtube
- consolidation tasks
- revisit recordings
- learn how to run scripts from the command line in python

code
- variables
- `print` 

strings
- `len()` counts the characters in a string
  - also other data types
- `.count("text")` counts all instances of "text" 
- `.lower` makes all characters lower case
- `.upper` makes all characters upper case
- `.capitalise` capitalises the first letter of sentences
- `.replace(,)` replaces one bit of text with another
- `print(<variable>[1:3])` - prints characters with the indexes 1 and 2 (format is [start:stop:step])

f strings
- `f"text"` - designed to cast for you, you can input variables of different data types into an f string and it will cast them into strings
- `(f"{(30/80) * 100:.2%}")` this gives the answer to decimal places and as a percentage
  - can also do `(percentage, 2)` on a normal round()

convert data types and concatenation
- Concatenation is joining strings together
- `str(<non-string variable>)`
- `int(<non-int variable>)`
- `float(<non-float variable>)`

data types and operations
- obvious ones
- `%` modulus gives remainder
  - 7 % 2 gives 1 as a remainder
- `<=`
- `>=`
- `!=`

Lists
- `[]` and separated by `,`
- work similarly to strings (e.g. `[0]` refers to first list item)
- `<list>[2] = <string>` replaces the third list item with a new item
- `.append()` adds one item to list
- `.extend()` adds multiple items to the list
- `.remove()` removes specific
- `.pop()` removes the last item

Dictionaries and their methods
- key: value pairs
- `dictionary(<key>)` gives the value for that key
- `dictionary[<key>] = ` amends the value of that key
- `.keys()` shows the dictionary keys (doesn't take arguments)
- `.values` shows the dictionary values (doesn't take arguments)
- `.items` returns key-value pairs as tuples (does not take arguments)
- `.get(key)` gets the value for a key
- `.pop(key)` removes and returns value for key
- `.update(dict)` merges in another dictionary
- `.setdefault(key, default)` sets default value if key is missing
- `.popitem()` removes and returns last inserted pair

Tuples
- immutable
  - cannot change elements, add or remove items, or sort or reverse it in place
- must reassign if you want to change it
- tuples are faster than lists
- can be used as dictionary keys
- `print(my_tuple[2])` prints item
- `print(my_tuple[:2])` slices item

## Functions
### What is a function?
- a reusable block of code that performs a specific task
- define a function once and then call it anywhere in your code

### Defining a function
`def greet():
`    print("hello")
- def = keyword to define function
- greet = function name
- () = parentheses (can contain parameters or arguments)
- : = start of the function block
- print("hello") = the function body

### Calling a function
`greet()` gives the output hello

### Function with parameters
`def greet(name):`
`    print(f"hello, {name}")`

`greet("Alice")`
`greet("Bob")`

### Function with return value
`def add(a, b):`
    `return a + b`

`result = add(3, 5)`
`print(result)`  
- Output: 8

## If statements
### What is an if statement?
- allows you to add conditions
- `if`
- `elif`
- `else:`


## For loops
### What is a for loop?
- a for loop goes through each item in a list (or other iterable) amd runs code for each item

### Basic syntax:
- `for item in collection:`
  - do something with item

### Example:
- `fruits = ["apple", "banana", "cherry"]`
- `for fruit in fruits:`
  - `print(fruit)`
- Output:
  - apple
  - banana
  - cherry

### Example with if statements
numbers = [1, 2, 3, 4, 5]

`for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")`

## While loops
### What is a while loop?
- A while loop keeps running as long as the condition is true
- It is used when you want something to keep running until a condition changes

### basic syntax and example
- `while condition:`
  - code runs while condition is true
- `count = 1`
- `while count <= 5:`
  - `print(count)`
  - `count += 1`

### Use `continue` to skip one round
- `x = 0`
- `while x < 5:`
    - `x += 1`
    - `if x == 3:`
      - `continue  # Skip printing 3`
    - `print(x)`






## Other stuff
- `input()` allows for user input
- `none` often used to initialise a variable when you dont have a real value to give it yet

converting to and from JSON and Yaml
- `json.dump` (dictionary) -> JSON-formatted string
- `json.dumps` (dictionary) -> JSON-formatted file
- `json.load` (JSON file) -> python dictionary
- `json.loads` (JSON-formatted string) -> python dictionary
- `yaml.dump` (dictionary) -> YAML string
- `yaml.safe_load` (YAML file) -> python dictionary

Converting between formats (python, JSON, YAML)
- `with open("<file name>", "w") as file:`
  - the `w` means write - you can write in that file
  - `r` means read only

git bash commands
- pwd - present working directory
- mkdir - make directory
- ls - list contents
- cd <folder> - change directory into that folder
- git init - initialises a repository with git
- git status
- git add 
- git commit -m ""
- git branch -M main - renames your master branch to main
- git remote add origin - this is the way your local repo will sync up with the remote storage location
- git push -u origin main - 
- git clone <URL> (of the remote repo)
- nano <folder> - command line text editor
- cat <folder> - shows the contents of the folder in the terminal

## JSON Library and HTTP requests

### JSON library

- `json.dump()` - write JSON data to a file
- `json.dumps()` - convert python to a JSON string
- `json.load()` - read JSON data from a file
- `json.loads()` - convert a JSON string to a python object

`import json
data = {"name": "Alice, "age": 25}
json_string = json.dumps(data)
print(json_string)`

- save to file
  - `with open("data.json", "w") as f:`
    - `json.dump(data, f)`
- load from file
  - `with open("data.json", "r") as f:`
    - `loaded_data = json.load(f)`

## Scripting
### Common uses for python scripts
- file processing - rename files, sort text, write logs
- data conversion - convert CSV to JSON
- Automation - backups, cleanup, reminders
- Web scraping - pull data from websites
- APIs and web tasks - fetch data, send requests
- Command-line tools - tools with arguments or options

### Libraries
- import this
- import random
  - `random.randint(1,10)`
- import math
  - `math.ceil`
  - `math.floor`
  - `math.pi`
- import os
- import sys
- import datetime
  - `datetime.date.today()`
  - `datetime.datetime.now()`
- import builtins
- import requests
  - `request.get(URL)`
  - `request.status_code`
  - `request.content`