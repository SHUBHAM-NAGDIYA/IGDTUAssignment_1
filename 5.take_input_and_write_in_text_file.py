#. Write a program that takes a string input from the user and writes it to a text file.
from pathlib import Path
s=input("Enter Something")

#path of text file
file=Path(r"C:\shubham data\shubham cse\IGDTU\IGDTU Assigment1\5.write_text_file.txt")
file.write_text(s)
