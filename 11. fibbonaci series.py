# Write a python program that generaite the first n numbers in the Fibonacci sequence.
num=int(input("Enter a number"))
n=0
n1=0
n2=1
print("Fibonacci series of ")
print(n1," ",n2,' ',end='')
for i in range(0,num-2):
    n=n1+n2
    n1=n2
    n2=n
    print(n," ",end='')