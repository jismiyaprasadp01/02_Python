'''
 Task 9: Directory Log Aggregator
 • Concepts: File I/O, directory traversal (using modules such as os or glob), string 
manipulation, and aggregation using dictionaries.
 • Description:
 Write a script that scans a specified directory for all .log files, processes each file, and 
aggregates counts of different log levels (e.g., INFO, WARNING, ERROR) into a single 
summary dictionary.
 • Validation:
 Place several sample log files in a test directory and verify that the aggregated counts 
correctly reflect the combined data from all files.
'''
import os

folder = "logs"
summary = {}

for file in os.listdir(folder):
    if file.endswith(".log"):
        with open(os.path.join(folder, file)) as f:
            for line in f:
                level = line.split()[0]
                summary[level] = summary.get(level, 0) + 1

print(summary)
