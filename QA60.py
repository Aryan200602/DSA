# program to find roots of the quadratic equation: 

import math
class Solution:
    
    def Roots(self, a, b, c):
        
        d = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(d))

        # Case when roots are real and different
        if d > 0:
            print("Roots are real and different")
            root1 = (-b + sqrt_val) / (2 * a)
            root2 = (-b - sqrt_val) / (2 * a)
            print(root1)
            print(root2)

        # Case when roots are real and same
        elif d == 0:
            print("Roots are real and same")
            root = -b / (2 * a)
            print(root)
            print(root)

        # Case when roots are complex
        else:
            print("Roots are complex")
            realPart = -b / (2 * a)
            print(f"{realPart} + i{sqrt_val}")
            print(f"{realPart} - i{sqrt_val}")

def main():
    a, b, c = 1, -3, -10

    obj = Solution()
    obj.Roots(a, b, c)

main()
