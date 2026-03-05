'''
Task 4: Modular Code Development
 Covers: Functions, modular programming, and data structures
 Description: Refactor the log parser into reusable functions, and group log entries by 
 severity using 
dictionaries.
'''
logs = ["ERROR Disk full", "INFO Server started", "ERROR File missing"]

def group_logs(logs):
    d = {}
    for l in logs:
        s = l.split()[0]
        d.setdefault(s, []).append(l)
    return d

print(group_logs(logs))
