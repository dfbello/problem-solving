# Collections - deque

from collections import deque

dq = deque()

with open("./input.txt", "r") as file:

	N = int(file.readline())

	for i in range(N):
		command = file.readline().split()
		if command[0] == "append":
			dq.append(int(command[1]))
		elif command[0] == "appendleft":
			dq.appendleft(int(command[1]))
		elif command[0] == "pop":
			dq.pop()
		else:
			dq.popleft()
		
print(*dq)		

