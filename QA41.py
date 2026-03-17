# Calculate the Power of a Number : Binary Exponentiation

def power(N, P):
    answer=1
    if P==0:
        return 1

    for i in range(P):
        answer*=N

    return answer

N=int(input("Enter the base number: "))
P=int(input("Enter the exponent: "))
print(power(N, P))