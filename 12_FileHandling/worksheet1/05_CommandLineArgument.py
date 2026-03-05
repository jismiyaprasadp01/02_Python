'''
 Task 5: Command-Line Tool
 Covers: Command-line argument parsing and list comprehensions
 Description: Create a script that accepts file names and search terms from the command line, 
processes logs, and outputs filtered results
'''
import sys

file = open(sys.argv[1])
word = sys.argv[2]

lines = [l for l in file if word in l]

for i in lines:
    print(i)
