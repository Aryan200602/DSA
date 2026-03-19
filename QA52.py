#Permutations in which N people can occupy R seats

# Solution class
class Solution:
    # Function to calculate nPr
    def permutation(self, n, r):
        # Initialize result
        ans = 1

        # Multiply n * (n-1) * ... * (n-r+1)
        for i in range(n, n - r, -1):
            ans *= i

        # Return result
        return ans

# Driver code
if __name__ == "__main__":
    # Create object of Solution class
    sol = Solution()

    # Input values
    n, r = 6, 4

    # Call permutation function
    result = sol.permutation(n, r)

    # Print result
    print(result)