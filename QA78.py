#Sum of the Numbers in a String

class Solution:
    # Function to calculate sum of numbers in a string
    def sumOfNumbers(self, s: str) -> int:
        total = 0
        temp = ""
        
        for c in s:
            if c.isdigit():
                temp += c
            else:
                if temp != "":
                    total += int(temp)
                    temp = "" 
        
        if temp != "":
            total += int(temp)
        
        return total


obj = Solution()
print(obj.sumOfNumbers("123xyz"))  
print(obj.sumOfNumbers("1xyz23"))  
