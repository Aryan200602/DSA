# reverse digit of the number

def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev

if __name__ == "__main__":
    number=int(input("Enter a number: "))
    result=reverse(number)
    print(f"The reverse of the number is: {result}")