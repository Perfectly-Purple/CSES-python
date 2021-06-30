a=int(input())
arr=input()
count=0
arr=arr.split(" ")
for i in range(len(arr)-1):
	if(int(arr[i])>=int(arr[i+1])):
		count+=int(arr[i])-int(arr[i+1])
		arr[i+1]=arr[i]
	else:
		continue
		
print(count)
