'''Log Parser
 Covers: String manipulation and regular expressions
 Description: Extract and format key details (timestamp, severity, message) from each log entry.'''
import re

line = "2026-03-05 10:20:30 ERROR Database connection failed"

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"

result = re.search(pattern, line)
print("Time:", result.group(1))
print("Severity:", result.group(2))
print("Message:", result.group(3))
