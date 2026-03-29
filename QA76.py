# Reverse a string 

# First method is simple using a stack, push and pop, as it follows the method of last in first out. 

def reverse_string(s):
    s=list(s)

    left=0
    right=len(s)-1

    while left<right:
        s[left], s[right]=s[right], s[left]

        left+=1
        right-=1

    return ''.join(s)

if __name__ == "__main__":
    s="hello world"
    print(reverse_string(s))
