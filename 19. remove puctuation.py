# Write a python program that removes all punctuation from a given string.

test_string = input("enter string")
 
print("The original string is : ", test_string)
 
# initializing punctuations string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
for elements in test_string:
    if elements in punctuations:
        test_string = test_string.replace(elements, "")
 
# printing result
print("The string after punctuation filter : ",test_string)