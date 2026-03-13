#Check if a number is Palindrome or Not

def palindrome(num):
    temp=num
    dig=0

    while num>0:
        rem=num%10
        dig=dig*10+rem
        num=num//10

    return temp==dig

if __name__=="__main__":
    num=121
    if palindrome(num):
        print("Palindrome")
    else:
        print("Not Palindrome")
