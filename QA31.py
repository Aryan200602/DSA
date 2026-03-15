# sum of n natural numbers

def sum(num):
    sum=0
    for i in range(1, num+1):
        sum+=i 
        return sum

if __name__=="__main__":
    num=10
    print("Sum of",num,"natural numbers is",sum(num))