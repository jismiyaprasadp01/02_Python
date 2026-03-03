'''
 Task 5: Command-Line Tool
 Covers: Command-line argument parsing and list comprehensions
 Description: Create a script that accepts file names and search terms from the command line, 
processes logs, and outputs filtered results
'''
import argparse

import re

def parse_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("search")

    return parser.parse_args()

def filter_log(filename,keyword):
    try:
        with open(filename,'r') as file:
            matches=[line.strip() for line in file if re.search(keyword,line,re.IGNORECASE)]
            return matches
        
    except FileNotFoundError:
        print("error: file not found")
        return []
    


args=parse_arguments()

res=filter_log(args.filename,args.search)

if res:
    print(f"\nFiltered Results ({len(res)} matches):")
    for line in res:
        print(line)
else:
    print("\nNo matching entries found.")
