def left_shift(arr, k):
    n = len(arr)

    for i in range(n - k):
        arr[i] = arr[i + k]

    for i in range(n - k, n):
        arr[i] = 0

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(left_shift(arr, k))