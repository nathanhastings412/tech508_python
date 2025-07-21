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

Dictionaries
- key: value pairs
- `dictionary(<key>)` gives the value for that key
- `dictionary[<key>] = ` amends the value of that key
- 

Other stuff
- `input()` allows for user input

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