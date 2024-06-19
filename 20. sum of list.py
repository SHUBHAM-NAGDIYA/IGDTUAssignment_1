list=[]
list_len=int(input("Enter the length of list"))
print("enter the list integer elments")
for i in range(0,list_len):
    n=int(input())
    list.append(n)

print("sum of list elements",sum(list))