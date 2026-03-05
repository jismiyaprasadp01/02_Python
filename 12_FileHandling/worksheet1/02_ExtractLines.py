'''
 Task 2: Log Filter
 Covers: File I/O and exception handling
 Description: Process a log file to extract lines containing "ERROR" and write them to a new file, 
handling missing files gracefully.
'''
try:
    file = open("log.txt", "r")
    newfile = open("error.txt", "w")

    for line in file:
        if "ERROR" in line:
            newfile.write(line)

    file.close()
    newfile.close()

    print("ERROR lines copied to error.txt")

except FileNotFoundError:
    print("Log file not found")
