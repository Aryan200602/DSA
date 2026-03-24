# Calculate the Area of the Circle

def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {area}")