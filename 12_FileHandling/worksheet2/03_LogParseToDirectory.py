''' Log Parser to Dictionary
 Develop a function that reads each line of the log file and parses it into a dictionary with 
keys: timestamp, log_level, module (if available), and message. Return a list of 
such dictionaries.
 Challenge: Handle lines that deviate from the standard format by either skipping them or 
recording an error message.'''

import re

pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<severity>[A-Z]+): \[(?P<tag>.*?)\] - (?P<message>.*)$"


def pattern_extract(s):
    match=re.match(pattern,s)
    if match:
        return {'timestamp': match.group('timestamp'),'severity':match.group('severity'),'tag':match.group('tag'),'message':match.group('message')}
    else:
        return "Line doesn't match standard format"
    
filename=input("Enter the log file name:")
try:
    file=open(filename,'r')
    content=file.readlines()
except FileNotFoundError:
    print("file does not exist!")
n=1
l=[]
for i in content:
    res=pattern_extract(i)
    #print('log - ',n,' ',res)
    l.append(res)
    n+=1

for i in l:
    print(i)
