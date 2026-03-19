#Express given number as Sum of Two Prime Numbers

class SumOf2Prime:

    # Function to check if a number is prime
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to express n as sum of two primes
    def findPrimeSum(self, n):
        for i in range(2, n):
            if self.isPrime(i) and self.isPrime(n - i):
                print(f"{n} = {i} + {n - i}")
                return
        print("No such combination exists")

# Driver code
n = 19
obj = SumOf2Prime()
obj.findPrimeSum(n)