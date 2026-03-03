'''Error Log Extractor
 Using basic string manipulation (without regex), write a script that filters and prints all log 
entries containing the word “ERROR”.
 Challenge: Verify that only well-formed error lines are extracted while ignoring 
misformatted lines.'''

def extract_error_logs(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                if "ERROR:" in line:
                    parts = line.split()
                    
                    if len(parts) >= 3 and parts[2].startswith("ERROR:"):
                        print(line)
                    else:
                        print(f"Ignored malformed line: {line}")
                 
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

log_file = input("Enter log file name: ").strip()
extract_error_logs(log_file)
