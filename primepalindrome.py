def isPrimePalindrome(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    s = str(n)
    return s == s[::-1]