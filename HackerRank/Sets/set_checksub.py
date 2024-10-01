# Sets - Check subset

A = set(map(int,input().split()))

n = int( input())

for i in range(n):

	B = set(map(int, input()split()))

	A_dff_B = A.diference(B)
	B_dff_A = B.diference(A)

	print(len(A_dff_B) >  0 and len(B_dff_A) == 0 )

	