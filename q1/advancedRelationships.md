# Advanced Class Relationships
## Previous Activities
Link to my previous activities:

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classImplementation.md)

[Part III - Class Relationships: Association and Multiplicity](classRelationships.md)

### Existing System Description

The system contains two classes: Eyeglasses and Customer. `Eyeglasses` stores information about a pair of glasses, while `Customer` stores a buyer and the eyeglasses they own. A customer can own zero or many pairs of eyeglasses, creating a one-to-many relationship.

### Inheritance Relationship

Parent: Eyeglasses

Child: ReadingGlasses

Explanation:

Reading glasses are a type of eyeglasses. They inherit all the common attributes and methods from the `Eyeglasses` class while adding a new attribute called `reading_distance`, making the design more organized and reducing duplicate code.

### Inheritance UML

Insert your UML image here.

```md
![Inheritance](images/inheritanceDiagram.png)
```

### Aggregation Relationship

Relationship: Customer HAS-A Eyeglasses

Type: Aggregation

Explanation:

A customer can own multiple pairs of eyeglasses, but each pair can still exist independently. If a customer is removed from the system, the eyeglasses object can still remain, so this is a weak HAS-A relationship (Aggregation).

### Advanced UML Diagram

Insert your complete UML diagram here.

```md
![Advanced UML](images/advancedClassDiagram.png)
```

### Python Implementation

```python


### Test Run

Insert your screenshot here.

```md
![Test](images/advancedTestRun.png)
```

### Object Diagram

Insert your object diagram here.

```md
![Objects](images/advancedObjectDiagram.png)
```

### Reflection

### 1\. Why did you choose your inheritance relationship?

I chose `ReadingGlasses` as the child class because it is a specific type of `Eyeglasses`. It shares the same basic attributes and behaviors while adding features unique to reading glasses.

### 2\. How did inheritance reduce duplicate code?

Inheritance allowed the child class to reuse the parent class's attributes and methods through `super().__init__()`. This prevented rewriting the same constructor and common methods.

### 3\. Why is your HAS-A relationship Aggregation?

The customer owns eyeglasses, but the eyeglasses can still exist without the customer. Because both objects have independent lifecycles, the relationship is aggregation.

### 4\. What is the difference between Association and the advanced relationship?

Association only shows that two classes are connected. Aggregation is more specific because it represents ownership while allowing both objects to exist independently.

### 5\. How does your design follow the DRY principle?

The `Eyeglasses` class stores all shared data and behavior in one place. `ReadingGlasses` inherits them instead of duplicating code, making the program easier to maintain.


