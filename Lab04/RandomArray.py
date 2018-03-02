import random


def getRandomDistr():
	return random.normalvariate(1, 2)

def genRandomArray(n):
	y=[]
	temp=[]
	summ=0
	for i in range(0,n):
		random=round(getRandomDistr(),2)
		temp.append(random)

	for j in range(len(temp)):
		summ+=temp[j]

	for k in range(len(temp)):
		y.append(temp[k] * (summ**-1 ) )

	return y



if __name__ == "__main__":
	n=int(input("enter count:"))
	y=genRandomArray(n)
	print(y)