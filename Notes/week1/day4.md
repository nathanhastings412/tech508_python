# Day 4

### Modules, libraries and packages

- look up more about scope
- add the other math operations to the math operations file
- DRY
  - Don't Repeat Yourself
- `from <document file name> import *` imports all the code in the document

What is a module?
  - the smallest piece of software in python
  - a single file
  - can give you extra functions
  - modules can import into other modules

What is a library?
- collection of modules

What is a package?
- packages are installable
- to install a package
  - in the terminal, type out:
    - pip install <package name>
  - go to python packages and search for the package then click install

notes
- if you go to terminal and `.venv` is not there you're virtual environment is not loaded up
- if virtual environment is not loaded and you install a pip, it will install a package to the global virtual environment

JSON:

    {
      "name" : "John Doe",
      "age" : 30,
      "isStudent" : false,
      "courses" : ["Python", "DevOps"],
      "address" : {
        "street" : "123 Main St",
        "city" : "Anytime",
      }
    }
- Uses [] for define lists
- Uses {} for dictionaries
- Double quotes for keys and string values
- Commas between list items and dictionary items

YAML:

    name: John Doe
    age: 30
    isStudent: false
    courses:
    - python
    - devops
    address:
    - street: 123 Main St
    - city: Anytown

- Uses hyphens for lists
- Strings don't need quotes
- Indenting is necessary for nested lists, dictionaries

### Scripting

What is scripting?
- Writing small, often quick-and-dirty
- used with the purpose:
  - automate a task
  - manipulate data
  - perform specific actions that don't need the complexity of a full application

