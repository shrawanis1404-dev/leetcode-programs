def countOdd(arr, n):
    count = 0
    for n in arr:
        if n % 2 != 0:
            count += 1
    return count