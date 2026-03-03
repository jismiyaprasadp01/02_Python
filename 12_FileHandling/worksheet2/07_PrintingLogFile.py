'''Command-Line Log Filter
 Develop a command-line tool using Python’s argparse module that accepts two 
arguments: a log level (e.g., “ERROR”) and a module name. The script should filter the log 
file to print only those entries matching both criteria.
 Challenge: Validate the command-line inputs and provide helpful error messages for invalid 
or missing arguments.'''
import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description="Filter log entries by search term.")
    parser.add_argument("filename", help="Path to the log file")
    parser.add_argument("search", help="Keyword or pattern to search for")
    return parser.parse_args()

def filter_logs(filename, keyword):
    try:
        with open(filename, "r") as file:
            matches = [line.strip() for line in file if re.search(keyword, line, re.IGNORECASE)]
            return matches
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


args = parse_arguments()
results = filter_logs(args.filename, args.search)
    
if results:
    print(f"\nFiltered Results ({len(results)} matches):")
    for line in results:
        print(line)
else:
    print("\nNo matching entries found.")
