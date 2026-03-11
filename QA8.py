#Rotate array by K elements : Block Swap Algorithm#

class solution:
    def rotate_array(self, arr, start, end):
        while start<  end:
            arr[start], arr[end]= arr[end], arr[start]
            start+=1
            end-=1

    def left_rotate(self, arr, d):#to rotate the array we rotate the first part, then the second and #
                                 #the complete array#
        n=len(arr)
        if d==0 or d==n:
            return 

        self.rotate_array(arr, 0, d-1)
        self.rotate_array(arr, d, n-1)
        self.rotate_array(arr, 0, n-1)

    def right_rotate(self, arr, d): #for right rotate use left rotate once again but pass the length-d elements#
        n=len(arr)
        self.left_rotate(arr, n-(d%n))

if __name__=="__main__":
    arr1=[1,2,3,4,5]
    k=3
    obj=solution()
    obj.left_rotate(arr1,k)
    print(f"the left rotated array is {arr1}")

    arr1=[1,2,3,4,5]
    obj.right_rotate(arr1,k)
    print(f"the right rotated array is {arr1}")
        