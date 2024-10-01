# Sets - No idea!

n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))


happy_level = 0

for i in arr:
	if i in a:
		happy_level += 1
	if i in b:
		happy_level -= 1

print(happy_level)
