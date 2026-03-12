#Replace elements by its rank in the array

class Solution:
    def replace(arr):
        sorted_arr=sorted(arr)
        rank_mp={}
        rank=1

        for element in sorted_arr:
            if element not in rank_mp:
                rank_mp[element]=rank
                rank+=1

        for i in range(len(arr)):
            arr[i]=rank_mp[arr[i]]
        return arr 

if __name__=="__main__":
    arr=[40,10,20,30]
    print(Solution.replace(arr))