#sum of the array#

class Solution:
    def sum_of_elements(self, arr):
        return sum(arr)

if __name__=="__main__":
    sol=Solution()
    arr1=[2,4,6,1,4]
    print(f"the sum of all the element in the array is {sol.sum_of_elements(arr1)}")