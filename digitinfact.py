def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(len(str(fact)))
n=int(input("enter a number"))
factorial(n)