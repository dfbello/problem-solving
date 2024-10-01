def isSubsequence(s, t):
	ps, pt = 0,0

	if len(s) == 0:
		return True
		
	while pt < len(t):

		if s[ps] != t[pt]:
			pt += 1
			continue
		else:	
			pt += 1
			ps += 1
			
		if ps == len(s):
			return True

	return False



s = "abc"
t = "a,fblowc"
print(isSubsequence(s,t))