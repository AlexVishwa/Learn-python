import os
import xlrd
# File handling is used to read, write and edit files
    # "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "t" - Text - Default value. Text mode
    # "b" - Binary - Binary mode (e.g. images)
# current_dir = os.path.dirname(__file__))
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'file1.txt')
f = open(file_path)
txt = f.read()
print(type(txt))
print(txt)
# print("Hello file")
f.close()

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '../day_19/file1.txt')
with open(file_path, 'w+') as f:  # Changed mode to 'w+'
    f.write('This text will be written in a newly created file')
    f.seek(0)  # Move the cursor to the beginning of the file
    txt = f.readlines()
    print(type(txt))
    print(txt)
    #print(f.read())

import csv
# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, '../day_19')
csv_file_path = os.path.join(current_dir, 'csv_examples.csv')
with open(csv_file_path) as f:
    csv_reader = csv.reader(f, delimiter=',') # we use the reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

#* Excel/XLS file
# import xlrd
# import os
# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, '../assets/Book1.xls')
# excel_book = xlrd.open_workbook(file_path)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)
# <bound method Book.sheet_names of <xlrd.book.Book object at 0x000001A7EA23B050>>