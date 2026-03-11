#Average of all the elements in the array#

class solution:
    def avg(self, arr, n):
        for i in range(len(arr)):
            if n==0:
                return 0
            arr[i]=arr[i]/n 
        return arr

if __name__=="__main__":
    arr1=[1,2,3,4,5]
    n=len(arr1)
    obj=solution()
    print(f"the average of the array is {obj.avg(arr1,n)}")