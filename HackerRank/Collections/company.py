# Collections - Company logo

from collections import Counter

with open("./input.txt" , "r") as file:

	s = file.readline().rstrip()


count = Counter(sorted(s))
result = ["{} {}".format(x,y) for x,y in count.most_common(3)]

print("\n".join(result))

