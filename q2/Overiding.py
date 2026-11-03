class Animal: 
  def __init__(self, name):
        self._name = name 

  def eat(self):
    return self.eat
    
  def make_sound(self):
    return self.make_sound

class lion(Animal):
    def __init__(self, name):
      self._name = name 
        
    def eat(self):
      print("eats fresh meat.")
        
    def make_sound(self):
      print("roars loadly!")

class elephant(Animal):
    def __init__(self, name):
      self._name = name 
        
    def eat(self):
      print("eats fresh meat.")
        
    def make_sound(self):
      print("trumpets!")

class monkey (Animal):
    def __init__(self, name):
      self._name = name 
        
    def eat(self):
      print("eats bananas!")
        
    def make_sound(self):
      print("chatters!")

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

