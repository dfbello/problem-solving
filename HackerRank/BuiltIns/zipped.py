# Built Ins - Zipped!!

with open("./input.txt", "r") as file:

	_, X = map(int, file.readline().split())
	subject_marks = []

	for i in range(X):
		s = list(map(float, file.readline().split()))
		subject_marks.append(s)

for student in zip(*subject_marks):
	print(sum(student)/X)

