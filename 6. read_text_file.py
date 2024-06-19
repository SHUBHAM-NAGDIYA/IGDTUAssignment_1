#. Write a program that reads the content of a text file and prints it to the console.

from pathlib import Path
content=Path(r"C:\shubham data\shubham cse\IGDTU\IGDTU Assigment1\5.write_text_file.txt")
Read=content.read_text()
print(Read)
