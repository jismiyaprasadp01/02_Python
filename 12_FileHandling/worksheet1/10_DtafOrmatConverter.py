'''Data Format Converter (CSV to JSON)
 • Concepts: File I/O, CSV and JSON modules, data transformation, and list comprehensions.
 • Description:
 Develop a script that reads data from a CSV file and converts each row into a JSON object. 
The final output should be a JSON file containing an array of these objects.
 • Validation:
 Provide a sample CSV file and confirm that the output JSON file accurately represents the 
CSV content structure.'''

import csv
import json

data = []

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open("data.json","w") as f:
    json.dump(data,f,indent=4)

print("CSV converted to JSON")
