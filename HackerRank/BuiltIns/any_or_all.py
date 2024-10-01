# Built ins - any or all

def check_palindrome(x):
	s = str(x)

	flag = True
	for i in range(len(s)//2):
		if s[i] is not s[-i-1]:
			flag = False
			break


	return flag




with open("./input.txt", "r") as file:

	file.readline()
	l = list(map( int, file.readline().split()))

if all([x>0 for x in l]):
	print(any([check_palindrome(x) for x in l]))
else:
	print(False)




