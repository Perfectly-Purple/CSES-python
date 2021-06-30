x=int(input())
y=input()
y=y.split(" ")
for i in range(len(y)):
	y[i]=int(y[i])
y.sort()
n,count=1,0
for i in y:
	if (i!=n):
		print(n)
		count+=1
		break
	n+=1
	
if(count==0):
	print(y[x-2]+1)
