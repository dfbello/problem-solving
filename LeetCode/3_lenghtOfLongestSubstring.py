def lengthOfLongestSubstring(s):
	start = 0

	last_seen = {}
	max_len = 0	

	for end in range(len(s)):
		if s[end] in last_seen and start <= last_seen[s[end]]:
			start = last_seen[s[end]] + 1
		last_seen[s[end]] = end
		max_len = max(max_len, end-start + 1)


	return max_len





s = "abceadve"

print(lengthOfLongestSubstring(s))
