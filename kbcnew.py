Question = ["What is the Python?", "What do you mean about coding?", "Who is co-founder of NAVGURUKUL?", "Who is the corrent DisCo of NAVGURUKUL?", "Who is the father of Computer?"]

First_option = ["Programing_languase", "Peer learning", "Abhisek Gupta", "Ravina", "Charles Cabise"]

Second_option = ["Programing", "all", "Anuradha", "Kajal", "charles babbage"]

Third_option = ["Languase", "Google search", "Rishav", "Komal", "einstein"]

Fourth_option = ["Snack", "Self learning", "Vandana", "Kajal and Komal", "No one"]

Ans_key = [0, 1, 2, 3, 1]
a = 0
sum = 0
while(a < 4):
	print Question[a]
	print "0.", First_option[a]
	print "1.", Second_option[a]
	print "2.", Third_option[a]
	print "3.", Fourth_option[a]
	user_ans = int(raw_input("Enter your Answer:- "))
	if (user_ans == Ans_key[a]):
		sum = sum + 1
		print "Wow! Right Answer."
	else:
		print "Oh! Wrong Answer."
	a = a + 1
print "Your Right answer is",sum
print Question[4]
print "0.", First_option[4]
print "1.", Second_option[4]
print "2.", Third_option[4]
print "3.", Fourth_option[4]
user_ans = int(raw_input("Enter your Answer:- "))
if user_ans == Ans_key[3]:
	sum = sum+1
	print "Wow! Right Answer."
else:
	print "Oh! Wrong Answer."
print "Your Right Answers are", sum,"/",len(Question) 
if (sum == 5):
	print "Congrats! You are winner of five crore."
elif (sum == 4):
	print "Congrats! You are winner of Three crore."
elif (sum == 3):
	print "Congrats! You are winner of one crore."
else:
	print "Sorry! You lossed your money."
print "**************Bye-Bye***************"
