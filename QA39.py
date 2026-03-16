# Print Fibonacci Series up to Nth term

def fib(N):
    if N<=1:
        return N 

    last=fib(N-1)
    second_last=fib(N-2)

    return last+second_last

N=int(input("Enter the number of terms: "))
for i in range(N+1):
    print(fib(i), end=' ')

