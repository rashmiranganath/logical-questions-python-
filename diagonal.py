list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
sum1=0
j=2
sum=0
while i<len(list):
	sum1=sum1+list[i][i]
	sum=sum+list[i][j]
	i=i+1
	j=j-1
if sum==sum1:
	print "diagonal hai"
else:
	print "not diagonal"

