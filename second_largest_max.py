def second_largest(arr):
    largest = arr[0]
    second = -1

    for i in range(1, len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]

    return second

arr = [10, 25, 5, 40, 30]
print(second_largest(arr))