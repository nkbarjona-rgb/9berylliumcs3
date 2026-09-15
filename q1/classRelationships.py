class Eyeglasses:
    def __init__(self, rim_type, grade, frame_shape):
        self.rim_type = rim_type
        self.grade = grade
        self.frame_shape = frame_shape

    def display_info(self):
        return f"{self.rim_type} | {self.grade} | {self.frame_shape}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.eyeglasses = []

    def add_eyeglasses(self, glasses):
        self.eyeglasses.append(glasses)

    def show_collection(self):
        print(f"\n{self.name}'s Eyeglasses:")
        for item in self.eyeglasses:
            print(item.display_info())


customer = Customer("Nikobitara")

g1 = Eyeglasses("Rimless", "Grade 100", "Round")
g2 = Eyeglasses("Full Rim", "Grade 200", "Square")
g3 = Eyeglasses("Semi Rimless", "Grade 150", "Oval")

print("--- BEFORE RELATIONSHIP ---")
print(g1.display_info())
print(g2.display_info())
print(g3.display_info())

print("\n--- BUILDING RELATIONSHIP ---")
customer.add_eyeglasses(g1)
customer.add_eyeglasses(g2)
customer.add_eyeglasses(g3)

print("\n--- AFTER RELATIONSHIP ---")
customer.show_collection()
