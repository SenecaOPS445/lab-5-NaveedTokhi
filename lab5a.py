#!/usr/bin/env python3
# Author ID: Naveed Tokhi

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file: # open file in read mode
        content = file.read() # read the file contents
        file.close()
    return content
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as file: # open file in read mode
        lines = file.read().splitlines() # read the file and split the lines
        file.close()
    return lines
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))