from array import *
x=int(input())
ele=0
arr=[]
for i in range(x):
	y=input()
	y=y.split()
	r=int(y[0])
	c=int(y[1])
	if(r>=c):
		if(r%2==0):
			ele=r**2-c+1
		else:
			ele=(r-1)**2+c
	else:
		if(c%2!=0):
			ele=c**2-r+1
		else:
			ele=(c-1)**2+r
	arr.append(ele)
	
for i in range(x):
	print(arr[i])
