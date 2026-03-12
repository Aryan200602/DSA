#find the quilibrium point of the array. 

class Solution:
    def equilibrium(arr):
        total_sum=sum(arr)
        left_sum=0

        for i in range(len(arr)):
            total_sum-=arr[i]

            if left_sum==total_sum:
                return i 

            left_sum+=arr[i]

        return -1 
    
if __name__=="__main__":
    arr=[-7, 1, 5, 2, -4, 3, 0]
    print(Solution.equilibrium(arr))
