class animal: # creates a parent class named animal
    def __init__(self, name):
        self._name = name # stores animals name as an attribute

    def eat(self): # defines the method for the animal to eat
        pass # placeholder since "def eat(self)" has no code

    def make_sound(self): # defines the method for the animals sound
        pass # acts as a placeholder since the method has no code yet

class lion(animal): # creates a subclass named "lion" inside parent class "animal"
    def make_sound(self):
        return f"{self._name} roars loudly!"

    def eat(self):
        return f"{self._name} eats fresh meat."

class elephant(animal):
    def make_sound(self):
        return f"{self._name} trumpets!"

    def eat(self):
        return f"{self._name} eats grass and fruits."

class monkey(animal):
    def make_sound(self):
        return f"{self._name} chatters!"

    def eat(self):
        return f"{self._name} eats bananas."

lion = lion("Simba")
elephant = elephant("Dumbo")
monkey = monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")
