# check if the number is a perfect number of not

def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i

    return sum==num

if __name__=="__main__":
    num=27
    if perfect(num):
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")