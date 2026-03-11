#Rearrange array in increasing-decreasing order#

class Solution:
    def rearrange_array(self, arr):
        arr.sort()
        n=len(arr)
        arr[n//2:]=reversed(arr[n//2:])
        return arr 

if __name__== "__main__":
    arr1=[2,4,6,1,4]
    obj=Solution()
    obj.rearrange_array(arr1)
    print(f"the rearranged array is {arr1}")