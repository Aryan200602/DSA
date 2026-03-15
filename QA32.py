# sum of ap

def ap(a, d, n):
    sum=0

    for i in range(n):
        sum=sum+a
        a=a+d
    return sum

if __name__ == "__main__":
    a=int(input("Enter the first term: "))
    d=int(input("Enter the common difference: "))
    n=int(input("Enter the number of terms: "))
    sum=ap(a, d, n)
    print("The sum of the AP is: ", sum)