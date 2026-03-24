# find the area of a circle given its radius
class Area:
    def area_of_circle(self, r):
        area = 3.14 * r * r  # Area = π * r²
        print("Area of circle is :", area)

# Driver code
n = 5  # Radius
obj = Area()
obj.area_of_circle(n)
                           
