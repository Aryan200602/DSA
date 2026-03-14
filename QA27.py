#check if the number is armstrong number

def armstrong(num):
    temp=num
    dig=0
    sum=0

    while num>0:
        rem=num%10
        dig=dig+1
        num=num//10

    num=temp

    while num>0:
        rem=num%10
        sum=sum+rem**dig
        num=num//10

    return temp==sum

if __name__=="__main__":
    num=154
    if armstrong(num):
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")