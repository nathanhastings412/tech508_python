# Python Object Oriented Programming

### What led to the development of OOP?
- clear separation between data programs were operating on and the code which was operating on that data
- That style of programming is called procedural programming
  - the code is one place and operates on the data that is in a separate place
- one approach to this problem was to combine the data elements with the operations on that data
- e.g.
  - customer entity
  - information about the customer on that entity
  - also information relating to the order from the customer combined with the information
- class - the data elements and operational elements make up the class

### What is OOP?
- OOP is a way of structuring your code by grouping data and functions together into "objects"
- These objects are created from classes, which act like blueprints or templates

### Key concepts of OOP
- class - a blueprint for creating objects
- object - an instance of a class
- attribute - a variable that belongs to an object 
- method - a function that belongs to an object
- inheritance - one class can inherit from another
- encapsulation - hiding internal details and only exposing what's necessary
- polymorphism - same method name can work differently depending on the object

### The benefits of OOP
- data and functions combined
- better modularity
- low coupling
- re-use easier
- closely modelling the real world

### the problems with procedural programming
- data separated from functions
- lack of modularity
- high coupling
- re-use difficult
- not modelling the real world

### the principles of OOP
- abstraction
- encapsulation
- inheritance
- polymorphism

## Abstraction
### an example of abstraction
- what makes up a car?
  - windows
  - seats
  - steering wheel
  - wheels
  - engine
  - headlights
  - body
  - doors
- operations might be part of abstraction
  - getting into car
  - driving car

### the unit of abstraction
- class - type of object
  - data class contains
  - methods/functions class performs
- object - instace of a class

## Encapsulation
### Encapsulation - how do i work this thing (car example)?
- we do not necessarily know how a car works
- we need to know how do i work this car
- provide a simple, consistent interface to use the opject
- hide data and implementation details inside
- Each class has a well-defined responsibility

