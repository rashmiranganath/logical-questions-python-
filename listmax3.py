list=[10,11,8,6,7,19,76]
i=0
a=0
b=0
while i<len(list):
	if list[i]>a and list[i]<a and list[i]>b:
		a=list[i]
		b=list[i]
	i=i+1
print b 
	

