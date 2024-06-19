from pathlib import Path
csv_file=Path(r"C:\Users\shubh\anaconda3\Lib\site-packages\pyarrow\include\arrow\csv\chunker.h")
csv_data=csv_file.read_text()
print(csv_data)