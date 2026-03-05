'''JSON Log Converter
 Write a script that converts the log file into a JSON file. Each log entry should be a JSON 
object containing the keys: timestamp, log_level, module, and message.
 Challenge: Ensure that the JSON output correctly represents all valid log entries while 
ignoring or flagging misformatted lines.
'''

import json

logs = []

with open("log.txt") as f:
    for line in f:
        parts = line.split()

        if len(parts) >= 4:
            log = {
                "timestamp": parts[0],
                "log_level": parts[1],
                "module": parts[2],
                "message": " ".join(parts[3:])
            }

            logs.append(log)

with open("logs.json","w") as f:
    json.dump(logs,f,indent=4)

print("JSON file created")
