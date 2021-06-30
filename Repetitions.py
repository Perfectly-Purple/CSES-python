dna=input()
c=dna[0]
count,max=0,0
for i in dna:
	if(i==c):
		count+=1
	else:
		if(max<count):
			max=count
		count=1
		c=i
if(max<count):
	max=count
print(max)
