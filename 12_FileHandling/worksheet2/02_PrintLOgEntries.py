'''Error Log Extractor
 Using basic string manipulation (without regex), write a script that filters and prints all log 
entries containing the word “ERROR”.
 Challenge: Verify that only well-formed error lines are extracted while ignoring 
misformatted lines.'''


with open("log.txt") as f:
    for line in f:
        words = line.split()

        if len(words) > 0 and words[0] == "ERROR":
            print(line.strip())
