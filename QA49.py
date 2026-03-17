#Check if the number is an abundant number or not

def abundant(N):
    sum=0
    for i in range(1,N):
        if N%i==0:
            sum+=i 
            if sum>N:
                return True 
    return False 

if __name__ == "__main__":
    N=19
    print(abundant(N))