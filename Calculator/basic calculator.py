# Basic calculator :

operators = input("Enter operator(+ - * /) : ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number :"))

if operators == '+':
    result = num1 + num2
    print(round(result,2))
elif operators == '-':
    result = num1 - num2
    print(round(result,2))
elif operators == '*':  
    result = num1 * num2
    print(round(result,2))
elif operators == '/':
    result = num1 / num2
    print(round(result,2))