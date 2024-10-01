# Sets - set.remove() .discard() .pop()
n = int(input())

s = list(map(int, input().split()))
s.reverse()
s = set(s)

N = int(input())
	
for i in range(N):

	command = input().split()
    if command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
    elif command[0] == "pop":
      	s.pop()

print(sum(s))



