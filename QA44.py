# Check if a number is a Strong Number or not

class Main:
  def strong(self, N):
    
    temp=N
    sum=0
    
    while (N>0):
      dig= N % 10
      fact=1
      
      for i in range(1,dig+1):
        fact=fact*i
      sum+=fact
      N=N//10
      
    if(temp==sum):
      result="YES"
    else:
      result="NO"
    
    return result
    
if __name__ == "__main__":
  N=134
  print(Main().strong(N))