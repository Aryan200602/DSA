# check palindrome numbers in a range

def palindrome(a, b):

    for i in range(a, b + 1):

        num = i
        dig = 0
        temp = i

        while num > 0:
            rem = num % 10
            dig = dig * 10 + rem
            num = num // 10

        if temp == dig:
            print(temp)


if __name__ == "__main__":
    a = 10
    b = 150
    palindrome(a, b)