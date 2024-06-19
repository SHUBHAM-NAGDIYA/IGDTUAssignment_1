test_string=input("enter string: ")
frequency={}
for i in test_string:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1

print("frequency of all characters:\n",frequency)
