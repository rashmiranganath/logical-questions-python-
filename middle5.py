num1=input("enter")
num2=input("enter")
num3=input("enter")
num4=input("enter")
num5=input("enter")
if num1<num2<num3>num4>num5 or num1<num4<num3>num2>num5 or num5<num4<num3>num2>num1 or num5<num2<num3>num4>num1:
	print num3
elif num1<num3<num2>num4>num5 or num1<num4<num2>num3>num5 or num5<num4<num2>num3>num1 or num5<num3<num2>num4>num1:
	print num2
elif num2<num3<num1>num4>num5 or num2<num4<num1>num3>num5 or num5<num4<num1>num3>num5 or num5<num3<num1>num4>num5:
	print num1
elif num1<num2<num4>num3>num5 or num1<num3<num4>num2>num5 or num5<num3<num4>num2>num1 or num5<num2<num4>num3>num1:
	print num4
elif num1<num2<num5>num3>num4 or num1<num3<num5>num2>num4 or num4<num3<num5>num2>num1 or num4<num2<num5>num3>num1:
	print num5
