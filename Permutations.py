x=int(input())
if(x==1):
	print("1")
elif(x>1 and x<4):
	print("NO SOLUTION")
else:
	for i in range(2,x+1,2):
		print(i, end=" ")
	for i in range(1,x+1,2):
		print(i, end=" ")
