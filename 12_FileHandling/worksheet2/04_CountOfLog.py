'''Group Logs by Module
write a function that groups log entries by their module. 
For each module, output the count of log entries.
 Challenge: Use dictionary comprehensions or iterative methods to build the grouped result'''
import re
from collections import defaultdict
pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<severity>[A-Z]+): \[(?P<tag>.*?)\] - (?P<message>.*)$"


def pattern_extract(s):
    match=re.match(pattern,s)
    if match:
        return {'timestamp': match.group('timestamp'),'severity':match.group('severity'),'tag':match.group('tag'),'message':match.group('message')}
    else:
        return None
    
filename=input("Enter the log file name:")
try:
    file=open(filename,'r')
    content=file.readlines()
except FileNotFoundError:
    print("file does not exist!")
n=1
d=defaultdict(list)
for i in content:
    res=pattern_extract(i)
    print('log - ',n,' ',res)
    if res:
        key=res['severity']
        d[key].append(res)
    n+=1

print('\n\n')
for severity, entries in d.items():
    print(f"\n=== {severity} ===")
    for entry in entries:
        print(f"{entry['timestamp']} [{entry['tag']}] - {entry['message']}")
