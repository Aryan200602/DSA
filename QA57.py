import math

# coefficients (dummy input)
a = 1
b = -3
c = 2

# calculate discriminant
d = b*b - 4*a*c

# find roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different:", root1, root2)

elif d == 0:
    root = -b / (2*a)
    print("Roots are real and same:", root)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Roots are complex:", real, "+", imag, "i and", real, "-", imag, "i")