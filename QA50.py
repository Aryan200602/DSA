#Sum Of Digits of A Number

class Solution:
    # Function to find digital root using formula
    def addDigits(self, num: int) -> int:
        # If number is zero, digital root is zero
        if num == 0:
            return 0

        # Use digital root formula: 1 + (num - 1) % 9
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    num = 472
    print(sol.addDigits(num))

    # Test case 2
    num = 102
    print(sol.addDigits(num))