list=[10,20,30,10,30,40]
i=0
new=[]
new1=[]
while i<len(list):
	count=0
	j=0
	while j<len(list):
		if list[i]==list[j]:
			count=count+1
		j=j+1
	new.append([list[i],count])
	if new[i] not in new1:
		new1.append(new[i])
	
	i=i+1
print new1
	
