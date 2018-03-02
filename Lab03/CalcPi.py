import time

def calcPi(n):
  return ( (4*n*n) / ( (2*n-1) * (2*n+1) ) )


start_time = time.time() #start 

epsilon=1e-17
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
  
  
print("--- %s seconds ---" % (time.time() - start_time)) #end  
print (pi*2)

#after 1*10^-16 stopped in case of bad method

