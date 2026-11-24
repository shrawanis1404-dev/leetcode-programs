arr = [2, 5, 1, 3, 4, 7]
n = 3

res = []

for i in range(n):
    res.append(arr[i])
    res.append(arr[i+n])

print("Original Array:", arr)
print("Shuffled Array:", res)