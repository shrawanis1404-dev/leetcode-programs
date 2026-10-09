
def diamondPattern(n: int) -> list[str]:
    k = (n + 1) // 2
    result = []

    
    for i in range(1, k + 1):
        spaces = k - i
        stars = 2 * i - 1
        result.append(" " * spaces + "*" * stars)

    
    for i in range(k - 1, 0, -1):
        spaces = k - i
        stars = 2 * i - 1
        result.append(" " * spaces + "*" * stars)

    return result
