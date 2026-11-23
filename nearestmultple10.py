n = int(input("Enter a number: "))

if n % 10 < 5:
    print((n // 10) * 10)
else:
    print((n // 10 + 1) * 10)