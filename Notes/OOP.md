# Object-oriented Programming OOP

###What led to the development of OOP?
- Clear separation between data programs were operating on and the code which was operating on that data
- That style of programming is called procedural programming
	- The code is one place and operates on the data that is in a separate place
- One approach to this problem was to combine the data elements with the operations on that data - e.g.
	○ Customer entity
	○ Information about the customer on that entity
	○ Also information relating to the order from the customer combined with the information
- Class - the data elements and operational elements make up the class

### What is OOP?
- OOP is a way of structuring your code by grouping data and functions together into "objects"
- These objects are created from classes, which act like blueprints or templates

### Key concepts of OOP
Concept			Description
Class			A blueprint for creating objects (e.g., a Car class)
Object			An instance of a class (e.g., your actual car built from the blueprint)
Attribute		A variable that belongs to an object (e.g., car.color)
Method			A function that belongs to an object (e.g., car.drive())
Inheritance		One class can inherit from another (e.g., ElectricCar inherits Car)
Encapsulation	Hiding internal details and only exposing what’s necessary
Polymorphism	Same method name can work differently depending on the object

### The benefits of OOP
- Data and functions combined
- Better modularity
- Low coupling
- Re-use easier
- Closely modelling the real world

### The problems with procedural programming
- Data separated from functions
- Lack of modularity
- High coupling
- Re-use difficult
- Not modelling the real world

### The principles of Object-Oriented Programming
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Abstraction
### An example of abstraction
- What makes up a car?
	○ Windows
	○ Seats
	○ Steering wheel
	○ Wheel
	○ Engine
	○ Headlights
	○ Brake lights
	○ Body
	○ Doors
		§ Operations might be part of abstraction
			□ Getting into car
			□ Driving car
### The unit of abstraction
- Class - type of object
	○ Data class contains
	○ Methods/functions class performs
- Object - instance of a class
	
## Inheritance
### Inheritance - different types of car vehicle
- many different kinds of cars
- certain things in common and also different
- There is a general idea of a car but they can be made to be specialised and different
- Inheritance in that differently specialised cars fall under CAR but CAR falls under VEHICLE
	- VEHICLE would be superclass of CAR
	- CAR would be subclass of VEHICLE