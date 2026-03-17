# Find the Greates common factor

# class Main:
#   def gcd(self, N1, N2):
    
#     for i in range(min(N1,N2),0,-1):
#       if N1%i==0 and N2%i==0:
        
#         return i 
        
#     return 1 
    
# if __name__=="__main__":
#   N1=20
#   N2=15
# obj=Main()
# result=obj.gcd(N1,N2)
# print(result)

#Answer with EUCLIDIAN ALGORITHM

class Main:
  def gcd(self, N1, N2):
    
    while N1>0 and N2>0 :
      
      if N1>N2:
        N1=N1 % N2
        
      elif N2>N1:
        N2=N1 % N1
        
    if N1==0:
      return N2
      
    return N1
    
if __name__=="__main__":
  N1=20
  N2=15
obj=Main()
result=obj.gcd(N1,N2)
print(result)