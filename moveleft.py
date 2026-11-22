def left_rotate(arr):
    n = len(arr)
    first = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = first

    return arr

arr = [10, 20, 30, 40, 50]
print(left_rotate(arr))