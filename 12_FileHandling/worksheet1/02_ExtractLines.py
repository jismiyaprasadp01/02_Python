'''
 Task 2: Log Filter
 Covers: File I/O and exception handling
 Description: Process a log file to extract lines containing "ERROR" and write them to a new file, 
handling missing files gracefully.
'''
try:
    with open('small_log.txt','r') as file:
        inp=file.readlines()

    with open('new_log.txt','w') as file:
        for i in inp:
            if 'ERROR' in i:
                file.write(i)
except FileNotFoundError:
    print("log file not found")


