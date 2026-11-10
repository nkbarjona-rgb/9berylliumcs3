class Animal: 
  def __init__(self, name):
        self._name = name 

  def eat(self):
    pass
    
  def make_sound(self):
    pass

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

lion.make_sound()
print(lion.eat()
print("-----")

elephant.make_sound()
print(elephant.eat()
print("-----")

monkey.make_sound()
print(monkey.eat()
print("-----")

