#Check if array is subset of another array

# Function to perform binary search to check if an element is present in the array
def b_search(elem, arr, n):
    start = 0
    end = n - 1

    # Perform binary search
    while start <= end:
        mid = (start + end) // 2

        # If element is found, return True
        if arr[mid] == elem:
            return True
        elif arr[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    return False  # If the element is not found

# Function to check if arr1[] is a subset of arr2[]
def is_subset(arr1, m, arr2, n):
    # Sort arr2[] for efficient binary search
    arr2.sort()

    # If arr1[] has more elements than arr2[], it cannot be a subset
    if m > n:
        return False

    # For each element in arr1[], check if it exists in arr2[]
    for i in range(m):
        present = b_search(arr1[i], arr2, n)  # Check if arr1[i] is present in arr2[]

        # If any element from arr1[] is not present in arr2[], return False
        if not present:
            return False

    # If all elements of arr1[] are found in arr2[], return True
    return True

# Driver code
if __name__ == "__main__":
    # Initialize arrays
    arr1 = [1, 3, 4, 5, 2]
    arr2 = [2, 4, 3, 1, 7, 5, 15]

    # Calculate the sizes of the arrays
    m = len(arr1)
    n = len(arr2)

    # Call the is_subset function
    ans = is_subset(arr1, m, arr2, n)

    # Output the result
    if ans:
        print("arr1[] is a subset of arr2[]")
    else:
        print("arr1[] is not a subset of arr2[]")