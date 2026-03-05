'''Format Validator with Exception Handling
 Create a script that reads the log file and identifies lines that do not match the expected log 
format. For each misformatted line, log a warning with its line number while continuing to 
process the rest of the file.
 Challenge: Ensure that your solution uses try-except blocks to catch and handle exceptions 
without crashing.'''


with open("log.txt") as f:
    line_no = 0

    for line in f:
        line_no += 1

        try:
            parts = line.split()

            timestamp = parts[0]
            level = parts[1]
            module = parts[2]
            message = " ".join(parts[3:])

            print("Valid log:", timestamp, level, module, message)

        except:
            print("Warning: Misformatted line at", line_no)
