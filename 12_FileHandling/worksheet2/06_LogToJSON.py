'''JSON Log Converter
 Write a script that converts the log file into a JSON file. Each log entry should be a JSON 
object containing the keys: timestamp, log_level, module, and message.
 Challenge: Ensure that the JSON output correctly represents all valid log entries while 
ignoring or flagging misformatted lines.'''
import re
import json

def convert_log_to_json(log_file, json_file):
    log_entries = []
    malformed_lines = []

    pattern = re.compile(r'^\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)$')

    with open(log_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            match = pattern.match(line)
            if match:
                entry = {
                    "timestamp": match.group(1),
                    "log_level": match.group(2),
                    "module": match.group(3),
                    "message": match.group(4)
                }
                log_entries.append(entry)
            else:
                malformed_lines.append({"line_number": line_number, "content": line})

    with open(json_file, 'w') as outfile:
        json.dump(log_entries, outfile, indent=2)

    print(f" Converted {len(log_entries)} log entries to JSON.")
    if malformed_lines:
        print(f" Skipped {len(malformed_lines)} malformed lines:")
        for error in malformed_lines:
            print(f"  Line {error['line_number']}: {error['content']}")

filename=input("Enter the filename:")
convert_log_to_json(filename, "logs.json")
