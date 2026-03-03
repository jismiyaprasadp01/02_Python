'''Format Validator with Exception Handling
 Create a script that reads the log file and identifies lines that do not match the expected log 
format. For each misformatted line, log a warning with its line number while continuing to 
process the rest of the file.
 Challenge: Ensure that your solution uses try-except blocks to catch and handle exceptions 
without crashing.'''

import re

pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<severity>[A-Z]+): \[(?P<tag>.*?)\] - (?P<message>.*)$"


def pattern_extract(s):
    match=re.match(pattern,s)
    if match:
        return {'timestamp': match.group('timestamp'),'severity':[match.group('severity'),match.group('tag')],'message':match.group('message')}
    else:
        return "Line doesn't match standard format"
    
filename=input("Enter the log file name:")
try:
    file=open(filename,'r')
    content=file.readlines()
except FileNotFoundError:
    print("file does not exist!")
n=1
for i in content:
    res=pattern_extract(i)
    print('log - ',n,' ',res)
    n+=1
