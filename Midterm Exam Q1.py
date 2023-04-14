class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Prompt the user for the measurement
measurement = input("Enter the radius or diameter of the circle: ")

# Try to convert the input to a float
try:
    measurement = float(measurement)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Create a Circle object based on the input
if measurement > 100:
    circle = Circle(diameter=measurement)
else:
    circle = Circle(radius=measurement)

# Print the area and perimeter of the circle
print("Area: %.2f" % circle.area())
print("Perimeter: %.2f" % circle.perimeter()