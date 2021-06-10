#!/bin/bash/python3

import sys
import argparse
from pathlib import Path

def add_prefix_to_file(s, n, is_prefix):
    files = {}
    msg = { 'no_file_matching': 'No files matching %s',
            'file_list_check': 'change file name of all these files?(y/n) \n =>',
            'new_name_exists': 'New name : %s is already taken. Please choose a different name'
          }
    
    # sorted files list by modification time ascending order
    for f in sorted(Path('.').glob(s), key=lambda f: f.stat().st_mtime):
        # exclude Directory and hidden file
        if f.is_file() and not f.name.startswith('.'):
            files[f] = ""
            print(f.name)

    if len(files) == 0:
        print(msg['no_file_matching'] % s)
        sys.exit()

    # check if files are correctly selected
    if input(msg['file_list_check']).strip().lower() == "y":
        new_name = ""
        temp_counter = 1
        
        # generate new name for file
        for f in files.keys():
            if is_prefix:
                files[f] =  n + "-" + f.name
            else:
                files[f] = n + "-" + str(temp_counter) + f.suffix
                temp_counter += 1

    # rename file
    for f, new_name in files.items():
        # check if file name is already taken
        if not Path(new_name).exists():
            f.rename(new_name)
        else:
            print(msg['new_name_exists'] % new_name)

if __name__ == '__main__':
    # Init parser
    parser = argparse.ArgumentParser(description='Add prefix to filename')

    parser.add_argument("-s", "--searching", help = 'Search pattern or word')
    parser.add_argument("-p", "--prefix", help = 'Add prefix')
    parser.add_argument("-n", "--new_name", help = 'New name with digit index suffix')
    parser.add_argument("-r", "--reanme", help= 'Rename files as defualt format = prefix-YYYY-MM-DD (modified date)')

    # Read arguments from command line
    args = parser.parse_args()

    # If searching words and prefix is not given exit the program
    if args.searching == None or (args.prefix == None and args.new_name == None):
        print("Please specify searching keyword and prefix")
        sys.exit()

    name = args.prefix if args.prefix != None else args.new_name 
    is_prefix = True if args.prefix != None else False
    
    add_prefix_to_file(args.searching, name, is_prefix)
