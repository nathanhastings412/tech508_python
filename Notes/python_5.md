# Day 5

### consolidation notes

- Why is sys module important?
  - it lets you access the command line argument to run the script
  - the first argument is the name of the python file you are trying to run
  - sys.argv is the list of arguments
- OS module
  - manage folders
  - add new and delete old
  - get system information for the computer

converting to and from JSON and Yaml
- `json.dump` (dictionary) -> JSON-formatted string
- `json.dumps` (dictionary) -> JSON-formatted file
- `json.load` (JSON file) -> python dictionary
- `json.loads` (JSON-formatted string) -> python dictionary
- `yaml.dump` (dictionary) -> YAML string
- `yaml.safe_load` (YAML file) -> python dictionary

### API Fundamentals

What is an API?
- Application Programming Interface - interface/intermediary to connect to systems/services
- Provides access to data or asks for a certain action to be done
- Built to represent and give access to certain resources
- Often to access resources such as customer data, images, videos, web pages

Why use APIS as a level 2 support engineer?
- Retrieve and manipulate data from external systems and services
- Manual or automated interactions with cloud systems, infrastructure, especially to perform configuration or administrative actions
- To help investigate, troubleshoot, diagnose and resolve issues
- Simulate a user's actions or workflow to try and reproduce the issue

RESTful APIs
- REST - Representational State Transfer
- refers to the type of architecture for the API
- Primarily for building web services that are lightweight scalable, scalable, easily maintainable

Design promises for REST APIs:
- Representation and data flow 
- messages
- URIs/naming of resources
- Stateless
- Caching

JSON example:
{
  "ID" : "1",
  "firstname" : "Joe",
  "surname" : "Bloggs",
  "email" : "joe.b@gmail.com"
}

XML example:
<customer>
  <ID>1</ID>
  <firstname>Joe</firstname>
  <surname>Bloggs</surname>
  <email>joe.b@gmail.com</surname>
</customer>

HTTP messages
- Use HTTP as the protocol
- Can use HTTPS

HTTP - request structure
- CRUD (Create, Read, Update, Delete)
- VERB - need to have a verb in our request
  - GET - read
  - POST - create
  - PUT - update (replaces whole record)
  - PATCH - update (replace a piece of data)
  - DELETE - delete
- URL
  - header information is in key:value pairs
  - content-type - would match what you are sending
  - date
  - accept-characterset
- Version 
  - version of the site
- note: get requests often don't need anything in the body whilst other crud requests do

HTTP - response structure
- Response code - status codes
  - 1xx - informational
  - 2xx - success
  - 3xx - redirection
  - 4xx - client error
  - 5xx - server error
- version included again

API REST: Stateful vs Stateless
- Stateful
  - Client sends limited information with its request
  - get a response back
  - They could then ask for more information based on the last request
  - the servers keep track of the "state" of the requests
- Stateless
  - Every request must contain all the required information for the response
  - the servers are not keeping track of the "state" (the information)

- when you make an API request you must document 

note: CLI = Command Line Interface
