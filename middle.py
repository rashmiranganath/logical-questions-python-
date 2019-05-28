num1=input("enter")
num2=input("enter")
num3=input("enter")
if num1<num2<num3 or num3<num2<num1:
	print num2
elif num2<num1<num3 or num3<num1<num2:
	print num1
elif num1<num3<num2 or num2<num3<num1:
	print num3
