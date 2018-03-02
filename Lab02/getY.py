print('Enter number')
x=int(input())

def check(x):
    if (x>=0) and (x<=255):
      print('Y=byte')
    elif (x>=-32768) and (x<=32768):
      print('Y=Integer')
    else :
      print('Y=Long')
    
check(x)