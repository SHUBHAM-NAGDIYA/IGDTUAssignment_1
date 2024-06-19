#. Write a python program that returns the minimum and maximum values in a list of numbers.
list=[]
list_len=int(input("Enter the length of list"))
print("enter the list integer elments")
for i in range(0,list_len):
    n=int(input())
    list.append(n)


list_len=len(list)
min=list[0]
max=list[0]
for i in range(1,list_len):
    if min>list[i]:
        min=list[i]
    if max<list[i]:
        max=list[i]
    
print("min value in list:",min)
print("max value in list:",max)