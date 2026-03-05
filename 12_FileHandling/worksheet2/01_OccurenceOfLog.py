'''Custom Log Filter with Criteria
 • Concepts: Advanced string manipulation, regular expressions, file I/O, and dictionary 
usage.
• Description:
 Write a script that reads a log file and filters entries based on custom criteria—such as logs 
within a specific time range or containing a particular keyword pattern. Employ regex to 
accurately extract and process these elements.
 • Validation:
 Run the script on sample log data and confirm that the filtered output matches the specified 
criteria.'''

import re

keyword = "ERROR"

with open("log.txt") as f:
    for line in f:
        if re.search(keyword, line):
            print(line.strip())
