#Write a python program that checks if two strings are anagrams of each other
a=0
b=0
str1=input("Enter first string")
str2=input("Enter second string")
for i,j in str1,str2:
    a+=ord(i)
    b+=ord(j)

if a==b:
    print("your strings are anagrams")
else:
    print("Your strings are not anagram")