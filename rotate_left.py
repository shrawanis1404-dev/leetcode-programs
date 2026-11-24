arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

n = len(arr)
k = k % n

for i in range(k):
    first = arr[0]

    for j in range(n-1):
        arr[j] = arr[j+1]

    arr[n-1] = first

print(arr)
