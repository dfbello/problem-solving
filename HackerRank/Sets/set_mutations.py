# Sets - set mutations

_ = input()

a = set(map(int, input().split()))
n = int(input())

for i in range(n):
	command = input().split()[0]
	s = set(map(int, input().split()))

	if command == "update":
		a.update(s)
	elif command == "intersection_update":
		a.intersection_update(s)
	elif command == "difference_update":
		a.difference_update(s)
	elif command == "symmetric_difference_update":
		a.symmetric_difference_update(s)


print(sum(a))