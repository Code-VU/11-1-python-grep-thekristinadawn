import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    count = 0
    file_name = open('mbox-long.txt','r')
    for line in file_name: 
        
        if re.search(regular_expression, line): 
            count += 1
            #print(count)
            #print(line)
    print(f'mbox.txt had {count} lines that matched',regular_expression)


if __name__ == '__main__':
    
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()