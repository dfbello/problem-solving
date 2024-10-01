# Sets - captain's room

k = int(input())

room_list = list(map(int,input().split()))

s = set(room_list)
res = set(s)


for i in s:
    if len(res) == 1:
        break
    count = 0
    for j in range(len(room_list)):
        if room_list[j] == i:
            count += 1
        if count > 1:
            res.remove(i)
            break
    


print(res.pop())