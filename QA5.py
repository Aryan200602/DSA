#count the frequecy of each element in the array#

from collections import defaultdict
class Solution:
    def Freq(arr, n):
        new_pc= defaultdict(int)
        for i in range (n):
            new_pc[arr[i]]+=1

        for key, value in new_pc.items():
            print(f"{key} {value}")

if __name__=="__main__":
    arr1=[2,4,6,1,4]
    n=len(arr1)
    Solution.Freq(arr1,n)