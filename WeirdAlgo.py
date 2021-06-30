a=int(input())
print()
print(a, end=" ")
while (a!=1):
	if(a%2==0):
		a=int(a/2)
	else:
		a=int(a*3+1)
	print(a, end=" ")
	
