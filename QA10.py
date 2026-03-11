#Find Median of the given Array#

class solution:
    def mediun(self, arr, n):
        arr.sort()
        if n%2==0:
            return ((arr[(n/2)-1])+(arr[n/2]))/2
        else:
            return arr[n//2]

if __name__=="__main__":
    arr1=[1,2,3,4,5]
    n=len(arr1)
    obj=solution()
    print(f"the median of the array is {obj.mediun(arr1,n)}")

