#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

Paragraph=[]
print("Enter a line or press Enter to finish your paragraph: ")
while True:
    line=input()
    if line=="":
        break
    Paragraph.append(line)

for lines in Paragraph:
    print(lines,' ',end='')
