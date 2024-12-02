import random
secore_count = 0

for count in range(10,100):
	random_number_one = random.randomlist(50,100)
	random_number_two = random.randomlist(50,100)	
	answer = random_number_one - random_number_two
	print(random_number_one,'-', random_number_two)
	useer_input = int(input("Enter answer"))
	if user_input == answer:
		print("correct")
		score_count+= 1
	else:
		print("wrong")
print("your score",score_count,"/10")