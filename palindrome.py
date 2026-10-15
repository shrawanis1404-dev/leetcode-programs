def isPalindrome(n):
    if n < 0:
        return False

    temp = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return temp == rev