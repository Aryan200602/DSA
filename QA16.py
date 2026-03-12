#Find all Symmetric Pairs in the array of pairs

def find_symetric_pairs(arr):
    mp={}

    for i in range(len(arr)):
        first, second=arr[i]

        if second in mp and mp[second]==first:
            print (f"({second} {first})", end=' ')
        else:
            mp[first]=second

arr=[(1,2), (3,4), (5,6), (2,1), (4,3), (7,8)]
find_symetric_pairs(arr)
