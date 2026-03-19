#Find the sum of numbers in the given range

def sum_of_range(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i 
    return sum

if __name__ == "__main__":
    start=1
    end=10
    print(sum_of_range(start,end))