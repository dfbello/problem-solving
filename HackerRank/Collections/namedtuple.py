# Collections - named tuple

from collections import namedtuple as nt



with open("./input.txt", "r") as file:

	N = int(file.readline())
	Student = nt("Student", file.readline())
	s_list = [Student(*file.readline().split()) for i in range(N)]
	print("{:.2f}".format(sum([int(x.MARKS) for x in s_list])/len(s_list)))



