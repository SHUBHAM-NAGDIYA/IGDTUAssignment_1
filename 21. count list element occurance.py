list=[]
list_len=int(input("Enter length of list\n"))
print("enter list elments")
for i in range(list_len):
    element=input()
    list.append(element)

specific_el=input("enter number for checking occurancy ")
el_occurancy=list.count(specific_el)
print(el_occurancy)