# Sets - Symmetric difference 

m = input()
a = set(map(int, input().split()))

n = input()
b = set(map(int, input().split()))

res = a.union(b).difference(a.intersection(b))
res = list(res)
res.sort()

res = list(map(str, res))



print("\n".join(res))



