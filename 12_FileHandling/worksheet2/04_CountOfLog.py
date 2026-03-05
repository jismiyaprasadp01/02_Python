'''Group Logs by Module
write a function that groups log entries by their module. 
For each module, output the count of log entries.
 Challenge: Use dictionary comprehensions or iterative methods to build the grouped result
'''


def group_logs(file):

    module_count = {}

    with open(file) as f:
        for line in f:
            parts = line.split()

            if len(parts) >= 3:
                module = parts[2]

                module_count[module] = module_count.get(module, 0) + 1

    return module_count


result = group_logs("log.txt")
print(result)
