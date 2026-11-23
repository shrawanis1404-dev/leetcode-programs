try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    op=input("Enput operator to perform operation:")
    if op=="+":
        print("Addition is:",num1+num2)
    elif op=="-":
        print("Subtraction is:",num1-num2)
    elif op=="*":
        print("Multiplication is:",num1*num2)
    elif op=="/":
        if num2!=0:
           print("Division is:",num1/num2)
    elif op=="//":
        print("Floor Division is:",num1//num2)
    elif op=="**":
        if num2!=0:
            print("Power is:",num1**num2)
    else:
        print("Invalid operator try again!")
except TypeError:
    print("Check the type of input provided")
except ValueError:
    print("Values for numbers not defined")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except :
    print("something went wrong check and then retry")


