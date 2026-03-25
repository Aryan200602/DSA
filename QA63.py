#convert a number from decimal to binary:

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

if __name__ == "__main__":
    n = 11
    print(decimal_to_binary(n))