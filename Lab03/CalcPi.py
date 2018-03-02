def calcPi(n):
  return ( (4*n*n) / ( (2*n-1) * (2*n+1) ) )

epsilon=1e-3
n=1
pi1=1
pi2=1
while True:
  pi1*=calcPi(n)

  n+=1
  pi2*=calcPi(n)
  print(pi1)
  
  if (abs(pi2-pi1)<epsilon):
    break
    print (pi*2)
    
    
    




