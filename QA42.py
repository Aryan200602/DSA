# find the factorial of a number

class Main:
    
    def fact(self, n):
        facts = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                facts.append(i)

                if i != n // i:
                    facts.append(n // i)

        for f in facts:
            print(f, end=" ")
        print()


if __name__ == "__main__":
    
    obj = Main()
    N = 8
    obj.fact(N)