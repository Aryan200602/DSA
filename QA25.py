# check if the number is prime

def prime(num):

    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    num = 29

    if prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")