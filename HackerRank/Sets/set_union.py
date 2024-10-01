# Sets - set.union()

n = input()

eng = set(map(int, input().split()))

m = input()

fra = set(map(int, input().split()))

print(len(eng.union(fra)))
