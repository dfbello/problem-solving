# Built Ins - evaluation 

with open("./input.txt", "r") as file:

	exp = file.readline().strip()

s = []
print(exp)
eval("s." + exp + "(3)")
print(s)


"""
USEFULL USE OF EVAL AND AN ALTERNATIVE
# ./exprs.txt contains a space separated list of expressions (method names)

Consider the code in ../Sets/set_mutations.py
------------------------------------------------------///
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
------------------------------------------------------///
INPUT FORMAT:
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.


A better way to do this is by using hasattr and getattr like this:
hasattr(object, expression): returns a boolean indicating if object has method expression
getattr(object, expresiion): returns a function object.expression() 
"""

with open("./exprs.txt", "r") as exp:
	_ = exp.readline()

	a = set(map(int, exp.readline().split()))
	n = int(exp.readline())

	for i in range(n):
	        command = exp.readline().strip().split()[0]
	        s = set(map(int, exp.readline().split()))

#--------------------------------------------------------------///
	        if hasattr(a, command):  

	        	method = getattr(a, command)
	        	method(s)
#--------------------------------------------------------------///

print(sum(a))