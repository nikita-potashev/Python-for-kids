def calcPi(n):
  return ( (4*n*n) / ( (2*n-1) * (2*n+1) ) )

epsilon=1e-10
n=1
pi1=1
pi2=1
pi=1
while True:
  pi1=calcPi(n)
  pi2=calcPi(n+1)
  pi*=calcPi(n)
  n+=1
  if (abs(pi2-pi1)<=epsilon):
    break
  
    
    
print (pi*2)



