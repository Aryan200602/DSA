# print all the prime factores of a given number  

class Main:
  def prime_factors(self,N):
    c=0
    vict=[]
    for i in range(2,N):
      if(N%i==0):
        for j in range(2,int (i**0.5)+1):
          if (i%j==0):
            c+=1
        if c<1:
          vict.append(i)
      c=0
    return vict
if __name__ == "__main__":
  N=90
  obj=Main()
  result=obj.prime_factors(N)
  print(result)
  
    
  