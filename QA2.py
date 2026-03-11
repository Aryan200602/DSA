#write a code to find the larget number in the array#

def find_largest_number(arr,n):
    max=arr[0]
    for i in range (1,n):
        if arr[i]>max:
            max=arr[i]
            return max

if __name__=="__main__":
    arr1=[2,4,6,1,4]
    n=len(arr1)
    max=find_largest_number(arr1,n)
    print(f"the largest number in the array is {max}")
