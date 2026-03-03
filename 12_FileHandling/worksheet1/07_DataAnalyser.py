'''
 Task 7: CSV Data Analyzer
 • Concepts: File I/O, data structures (lists and dictionaries), list comprehensions, and basic 
data analysis.
 • Description:
 Develop a script that reads a CSV file containing columns such as "TestCase," "Status," and 
"ExecutionTime." The script should produce a summary report showing counts for each 
status (e.g., Passed, Failed) and compute the average execution time.
 • Validation:
 Use a sample CSV file and compare the output summary with expected statistics.
'''
import csv

from collections import defaultdict


def analyse_csv(filename):
    stat_count=defaultdict(int)
    total_time=0.0
    test_count=0

    with open(filename,newline='') as file:
        reader=csv.DictReader(file)
        for row in reader:
            status=row["Status"]
            time=float(row["ExecutionTime"])
            stat_count[status]+=1
            total_time+=time
            test_count+=1
            avg_time = total_time / test_count if test_count > 0 else 0

    return {
        "status_counts": dict(stat_count),
        "average_execution_time": round(avg_time, 2)
    }





filename=input("enter filename:")

res=analyse_csv(filename)
print("Test Status Counts:", res["status_counts"])
print("Average Execution Time:", res["average_execution_time"])


