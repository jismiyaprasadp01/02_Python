'''
Task 8: JSON Configuration Updater
 • Concepts: File I/O, JSON processing, dictionary manipulation, and exception handling.
 • Description:
 Create a script that loads a JSON configuration file, updates specific keys based on given 
conditions (for example, updating a version number or toggling a feature flag), and writes 
the modified configuration back to disk.
• Validation:
 Test the script with a sample JSON file and ensure only the intended keys are modified 
while the rest of the configuration remains intact.
'''
import json

with open("config.json","r") as f:
    data = json.load(f)

data["version"] = "2.0"
data["feature_enabled"] = True

with open("config.json","w") as f:
    json.dump(data,f,indent=4)

print("Configuration Updated")
