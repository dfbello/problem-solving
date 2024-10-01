def isVowel(c):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

	if c in vowels:
		return True

def reverseVowels(s):

	l = 0
	r = len(s) - 1

	s = list(s)
	while l < r:

		if not isVowel(s[l]):
			l += 1
			continue
		if not isVowel(s[r]):
			r -= 1
			continue

		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1



	return "".join(s)


s = "leetcode"
print(reverseVowels(s))