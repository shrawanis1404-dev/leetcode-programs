def right_shift(arr, k):
    n = len(arr)

    for i in range(n-1, 0, -1):
        if i >= k:
            arr[i] = arr[i-k]

    for i in range(k):
        arr[i] = 0

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(right_shift(arr, k))