'''Regular Expression Challenge (IP Address Extractor)
 Write a Python function that uses a regular expression to extract all unique IPv4 addresses 
from the log file. Some log messages include IP addresses (e.g., “Ping to server  succeeded”). Return a list of unique IP addresses found.
 Challenge: Ensure your regex correctly matches typical IPv4 formats and does not capture 
invalid patterns.'''

import re

def extract_unique_ips_from_file(filename):
   
    ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}'r'(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\b'

    ip_set = set()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            matches = re.findall(ip_pattern, content)
            ip_set.update(matches)
    except Exception as e:
        print(f"Error reading {filename}: {e}")

    return list(ip_set)


file=input("enter filename:")
l=extract_unique_ips_from_file(file)

for i in l:
    print(i)
