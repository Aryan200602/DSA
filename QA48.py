#check if the given number is Harshad(Or Niven) Number

def harshad(N):
    sum_of_digits=0
    temp=N
    digit=0
    while temp>0:
        digit=temp%10
        sum_of_digits+=digit
        temp//=10
    if N%sum_of_digits==0:
        return True 
    return False

if __name__ == "__main__":
    N=379
    print(harshad(N))