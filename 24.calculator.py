#. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
print('''choose a number for any mathemaitcle operation
         1. +
         2.-
         3.*
         4./
         5.%''')

operation=int(input())
num1=eval(input("enter first number"))
num2=eval(input("enter second number"))
if operation==1:
    print("sum=",num1+num2)

elif operation==2:
    print("subtraction=",num1-num2)

elif operation==3:
    print("multiplication=",num1*num2)

elif operation==4:
    print("division=",num1/num2)

elif operation==5:
    print("modula=",num1%num2)
