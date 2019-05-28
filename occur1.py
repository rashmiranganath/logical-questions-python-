list=[10,76,54,20,30,40]
i=0
new=[]
while i<len(list):
	j=i+1
	while j<len(list):
		new.append([list[i],list[j]])
		j=j+1
	i=i+1
print new
		
