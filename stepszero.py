def number_of_steps(n: int) -> int:
    steps = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1

        steps += 1

    return steps


n = 14
print(number_of_steps(n))