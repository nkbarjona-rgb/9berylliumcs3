class Eyeglasses:
    def __init__(self, frame_shape, rim_type, size, grade, material):
        self.frame_shape = frame_shape
        self.rim_type = rim_type
        self.size = size
        self._grade = grade
        self._material = material

    def wear(self):
        print(f"Wearing {self.frame_shape} eyeglasses.")

    def clean(self):
        print("Eyeglasses cleaned.")

class ReadingGlasses(Eyeglasses):
    def __init__(self, frame_shape, rim_type, size, grade, material, reading_distance):
        super().__init__(frame_shape, rim_type, size, grade, material)
        self.reading_distance = reading_distance

    def magnify_text(self):
        print(f"Best reading distance: {self.reading_distance} cm")

class Customer:
    def __init__(self, name):
        self.name = name
        self.eyeglasses = []

    def add_eyeglasses(self, glasses):
        self.eyeglasses.append(glasses)

# Test Run
glasses = ReadingGlasses(
    "Round",
    "Full Rim",
    14,
    100,
    "Polycarbonate",
    35
)

customer = Customer("Nikobitara")
customer.add_eyeglasses(glasses)

glasses.wear()
glasses.clean()
glasses.magnify_text()

print(f"\n{customer.name} owns {len(customer.eyeglasses)} pair(s) of eyeglasses.")
```
