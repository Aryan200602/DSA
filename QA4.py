#Reverse a given array#
class Solution:
    def reverse_array(self,arr):
        arr[:]=arr[::-1]

if __name__=='__main__':
    arr=[1,2,3,4,5]
    obj=Solution()
    obj.reverse_array(arr)
    print(f"the reversed array is {arr}")

"""
class Solution:
    # Function to reverse the array in-place
    def reverseArray(self, arr):
        # Initialize pointer to the beginning of the array
        p1 = 0

        # Initialize pointer to the end of the array
        p2 = len(arr) - 1

        # Loop until the two pointers meet in the middle
        while p1 < p2:
            # Swap the elements at p1 and p2
            arr[p1], arr[p2] = arr[p2], arr[p1]

            # Move the left pointer one step to the right
            p1 += 1

            # Move the right pointer one step to the left
            p2 -= 1

# Driver code
if __name__ == "__main__":
    # Create a Solution object
    sol = Solution()

    # Input array
    arr = [1, 2, 3, 4, 5]

    # Call the reverse function
    sol.reverseArray(arr)

    # Print the reversed array
    print(" ".join(map(str, arr)))
"""


