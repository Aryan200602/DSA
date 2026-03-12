#removing duplicatate in unsorted array#

class Solution:
    # Method to remove duplicates from array
    def remove_duplicates(self, arr):
        result = []
        seen = set()
        for val in arr: #this brings out the direct valure rather than the index, for index its- for i in range(len(arr))
            if val not in seen:
                result.append(val)
                seen.add(val)
        return result

# Driver code
if __name__ == "__main__":
    arr = [4, 5, 4, 2, 2, 3, 1]
    sol = Solution()
    result = sol.remove_duplicates(arr)
    print("Array after removing duplicates:", result)