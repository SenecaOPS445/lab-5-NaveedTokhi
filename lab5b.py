#!/usr/bin/env python3
# Author ID: Naveed Tokhi

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        content = file.read()
        file.close()
    return content


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        file.close()
    return lines


def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    """
     take two strings: file_name and string_of_lines
        open the file in append mode
        write the string to the file
    """
    with open(file_name, 'a') as file:
        file.write(string_of_lines)


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    """
    take two strings: file_name and list_of_lines
        open the file in write mode
        write each item from the list to the file
    """
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    """
    take two strings: file_name_read and file_name_write
        open the first file in read mode
        open the second file in write mode
        read the lines from the first file
        write the lines to the second file with line numbers
    """
    with open(file_name_read, 'r') as read_file:
        lines = read_file.read().splitlines()
        
    with open(file_name_write, 'w') as write_file:
        for idx, line in enumerate(lines, start=1):
            write_file.write(f'{idx}:{line}\n')

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))