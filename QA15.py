#Find all non-repeating elements in an array

from collections import Counter

def find_non_repeating(arr):
    el=Counter(arr)

    for element, count in el.items():
        if count ==1:
            print (element, end=' ')

arr=[1,2,3,4,5,2,6,7,8,9,1]
find_non_repeating(arr)