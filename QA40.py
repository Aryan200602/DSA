# Factorial of a Number : Iterative and Recursive

def fact(N):
    if N==0 or N==1:
        return 1

    return N*fact(N-1)

N=int(input("Enter a number: "))   
print(fact(N))