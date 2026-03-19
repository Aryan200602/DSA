#Program to Add two fractions

class Solution:
    # Function to compute gcd
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # Function to add two fractions
    def addFractions(self, num1, den1, num2, den2):
        
        lcm = (den1 * den2) // self.gcd(den1, den2)

        
        newNum1 = num1 * (lcm // den1)
        newNum2 = num2 * (lcm // den2)

       
        resultNum = newNum1 + newNum2
        resultDen = lcm

        
        common = self.gcd(resultNum, resultDen)
        resultNum //= common
        resultDen //= common

        print(f"{resultNum}/{resultDen}")


sol = Solution()
sol.addFractions(1, 3, 1, 6)  