arr = [1, 0, 2, 3, 0, 4, 5, 0]

n = len(arr)
res = []

for i in arr:
    res.append(i)

    if i == 0:
        res.append(0)

res = res[:n]

print(res)