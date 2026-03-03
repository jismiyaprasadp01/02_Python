'''
Task 4: Modular Code Development
 Covers: Functions, modular programming, and data structures
 Description: Refactor the log parser into reusable functions, and group log entries by 
 severity using 
dictionaries.
'''
import re

from collections import defaultdict


pattern=r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<severity>[A-Z]+): \[(?P<tag>.*?)\] - (?P<message>.*)$"


def pattern_find(s):
    match=re.match(pattern,s)
    if match:
        return {'timestamp': match.group('timestamp'), 'severity': match.group('severity'),'tag':match.group('tag'),'message': match.group('message')}
    else:
        return None




filename=input("enter file name:")

try:
    file=open(filename,"r")
    info=file.readlines()

except FileNotFoundError:
    print("log file not found")

dict1=defaultdict(list)
n=1
for line in info:
    res=pattern_find(line)
    print("log->",n,': ',res)
    if res:
        key=res['severity']
        dict1[key].append(res)
    n+=1

print('\n\n')
for key, values in dict1.items():
    print(f"\n{key}:")
    for i in values:
        print(f"{i['timestamp']} [{i['tag']}] - {i['message']}")


