#Second Smallest and Second Largest element in an array#

def find_second_smallest(arr,n):
    if n<2:
        return -1

    s=float('inf')
    ss=float('inf')

    for i in range(n):
        if arr[i]<s:
            s=arr[i]
            ss=s
        elif arr[i]<ss and arr[i]!=s:
            ss=arr[i]
        return ss 

def find_second_larget(arr,n):
        if n<2:
            return -1

        l=float('-inf')
        sl=float('-inf')

        for i in range(n):
            if arr[i]>l:
                l=arr[i]
                sl=l
            elif arr[i]>sl and arr[i]!=l:
                sl=arr[i]
            return sl

if __name__ == "__main__":
        arr1=[2,4,6,1,4]
        n=len(arr1)
        ss=find_second_smallest(arr1,n)
        sl=find_second_larget(arr1,n)
        print(f"the second smallest number in the array is {ss}")
        print(f"the second largest number in the array is {sl}")


