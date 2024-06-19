#25. Write a program that copies the contents of one text file to another
from pathlib import Path
from shutil import copy

source_file=Path("C:\shubham data\shubham cse\IGDTU\IGDTU Assigment1\print.txt")
dest_file=Path("C:\shubham data\shubham cse\IGDTU\IGDTU Assigment1\print_file2.txt")
dest_file.write_text(source_file.read_text())
