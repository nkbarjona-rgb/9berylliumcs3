# Class Relationships: Association and Multiplicity
## Previous Activities
Links to my previous activities:

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classImplementation.md)


## Existing Class
Class: Eyeglasses

Description: maya


## New Related Class
Class: Customer

Description: Represents a customer who buys many eyeglasses


## Association
Relationship: Customer HAS-A Eyeglasses

Action Phrase: "owns" 


## Multiplicity
Multiplicity: 1 : 0 (One To Many)

Explanation: A customer can own zero or many pairs of eyeglasses, while each eyeglasses object belongs to one customer. This lets us store multiple object references in a Python List. (rewrite)


## UML Class Relationship Diagram
![Class Relationship Diagram](link sa iamage folder

## Python Implementation
[View Python Source](classRelationships.py)


## Test Run
![Relationship Test Run](link sa image folder


## Object Relationship Diagram
![Object Relationship Diagram](link sa image folder


## Analysis
### What is the association between your two classes?

### What multiplicity did you choose and why?

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?

### LLM Prompt Used
![alt text](Images/Prompt.png)
