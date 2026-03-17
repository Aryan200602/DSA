# find if the number is automorphic or not

class Main:
  def automorphic(self, N):
    
    sqr=N*N
    
    while (N>0):
      
      if N%10 != sqr%10 :
        return False
      
      N=N//10
      sqr=sqr//10
      
    return True
    
if __name__ == "__main__":
  N=76
  print(Main().automorphic(N))
  