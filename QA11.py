#Remove Duplicates in-place from Sorted Array#

class solution:
    def dup(self, arr, n):
        if n == 0 or n == 1:
            return n
        
        j = 0
        
        for i in range(n - 1):
            if arr[i] != arr[i + 1]:
                arr[j] = arr[i]
                j += 1
        
        # Add the last element
        arr[j] = arr[n - 1]
        j += 1
        
        return j


if __name__ == "__main__":
    arr1 = [1,2,2,3,6,6,7]
    n = len(arr1)
    obj = solution()
    new_length = obj.dup(arr1, n)
    
    print("Array after removing duplicates:", arr1[:new_length])