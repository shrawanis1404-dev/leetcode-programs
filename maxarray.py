def find_max(arr: list[int]) -> int:
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum


arr = [10, 25, 7, 40, 15]
print(find_max(arr))

