# Sets - set.difference()

n = input()

eng = set(map(int, input().split()))

m = input()

fra = set(map(int, input().split()))

res = eng.union(fra).difference(eng.intersection(fra))


print(len(res))
