def insert_element(arr, x, p):
    n = len(arr)

    for i in range(n-1, p, -1):
        arr[i] = arr[i-1]

    arr[p] = x

    return arr

arr = [10, 20, 30, 40, 50]
x = 99
p = 2

print(insert_element(arr, x, p))