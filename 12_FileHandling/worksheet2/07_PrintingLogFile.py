'''Command-Line Log Filter
 Develop a command-line tool using Python’s argparse module that accepts two 
arguments: a log level (e.g., “ERROR”) and a module name. The script should filter the log 
file to print only those entries matching both criteria.
 Challenge: Validate the command-line inputs and provide helpful error messages for invalid 
or missing arguments.
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("level", help="Log level (INFO, ERROR, WARNING)")
parser.add_argument("module", help="Module name")

args = parser.parse_args()

with open("log.txt") as f:
    for line in f:
        parts = line.split()

        if len(parts) >= 3:
            log_level = parts[1]
            module = parts[2]

            if log_level == args.level and module == args.module:
                print(line.strip())
