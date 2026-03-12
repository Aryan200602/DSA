#Find all repeating elements in an array

from collections import Counter

def find_repeating_element(arr):
    element_count=Counter(arr)

    for element, count in element_count.items():
        if count > 1:
            print (element, end=' ')
    
arr=[1,2,3,4,5,2,6,7,8,9,1]
find_repeating_element(arr)
