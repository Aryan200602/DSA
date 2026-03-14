# check for even or odd number

def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

if __name__=="__main__":
    num=27
    print(num,"is an",even_odd(num),"number")