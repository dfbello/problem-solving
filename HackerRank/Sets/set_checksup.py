# Sets - Check strict superset

A = set(map(int,input().split()))

n = int( input())

flag = True

for i in range(n):
    B = set(map(int, input().split()))

    A_dff_B = A.difference(B)
    B_dff_A = B.difference(A)
    
    if not (len(A_dff_B) > 0 and len(B_dff_A) == 0):
        flag = False
        break

print(flag)
