class Eyeglasses:

    def __init__(
        self,
        frame_shape: str,
        rim_type: str,
        size: int,
        grade: int,
        material: str,
    ):
        # Public attributes
        self.frame_shape = frame_shape
        self.rim_type = rim_type
        self.size = size  # Size in cm (int)

        # Private attributes
        self.__grade = grade  # Prescription grade as integer
        self.__material = material  # Material description

    # Method that reads a private attribute
    def get_grade(self) -> int:
        return self.__grade

    # Method that reads a private attribute
    def get_material(self) -> str:
        return self.__material

    # Method receiving a parameter and safely modifying a private attribute
    def update_grade(self, new_grade: int):
        if new_grade != 0:
            self.__grade = new_grade
            print(f"[{self.frame_shape}] Prescription updated to {new_grade}.")
        else:
            print("Grade update must be a non-zero integer.")

    # Method modifying private material state safely
    def change_material(self, new_material: str):
        if new_material:
            self.__material = new_material
            print(f"[{self.frame_shape}] Material updated to {new_material}.")
        else:
            print("Material description cannot be empty.")


reading_glasses = Eyeglasses(
    frame_shape="Rectangular",
    rim_type="Full-rim",
    size=14,
    grade=1,
    material="Polycarbonate",
)
myopia_glasses = Eyeglasses(
    frame_shape="Round",
    rim_type="Semi-rimless",
    size=13,
    grade=-2,
    material="High-Index Plastic",
)

print("--- BEFORE ---")
print(
    f"Reading Glasses ({reading_glasses.frame_shape}) Grade: {reading_glasses.get_grade()}"
)
print(
    f"Myopia Glasses ({myopia_glasses.frame_shape}) Grade: {myopia_glasses.get_grade()}"
)

print("\nPerforming action on Reading Glasses...")
reading_glasses.update_grade(2)

print("\n--- AFTER ---")
print(
    f"Reading Glasses ({reading_glasses.frame_shape}) Grade: {reading_glasses.get_grade()}"
)
print(
    f"Myopia Glasses ({myopia_glasses.frame_shape}) Grade: {myopia_glasses.get_grade()}"
)
