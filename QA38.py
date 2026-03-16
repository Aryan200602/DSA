# Python program to find maximum and minimum digit in a number

class Solution:
    def findMaxMinDigit(self, n):
        # Initialize max and min digits
        maxDigit = 0
        minDigit = 9

        # Traverse digits one by one
        while n > 0:
            # Extract last digit
            digit = n % 10

            # Update max digit
            if digit > maxDigit:
                maxDigit = digit

            # Update min digit
            if digit < minDigit:
                minDigit = digit

            # Remove last digit
            n = n // 10

        # Print result
        print("Max Digit:", maxDigit)
        print("Min Digit:", minDigit)

# Input number
n = 93824

# Create object and call function
obj = Solution()
obj.findMaxMinDigit(n)