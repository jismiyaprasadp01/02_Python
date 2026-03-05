''' Log Parser to Dictionary
 Develop a function that reads each line of the log file and parses it into a dictionary with 
keys: timestamp, log_level, module (if available), and message. Return a list of 
such dictionaries.
 Challenge: Handle lines that deviate from the standard format by either skipping them or 
recording an error message.'''


def parse_log(file):

    logs = []

    with open(file) as f:
        for line in f:
            parts = line.split()

            if len(parts) >= 3:
                log = {
                    "timestamp": parts[0],
                    "log_level": parts[1],
                    "message": " ".join(parts[2:])
                }

                logs.append(log)

    return logs


result = parse_log("log.txt")
print(result)
