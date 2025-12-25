"""
Today’s goal is to work with files and analyze logs using Python.
I will create a Python script that:
Reads a log file (example: application or system log)
Identifies and counts:
INFO
WARNING
ERROR messages
Prints a summary to the terminal
Writes the summary to an output file
This task introduces you to one of the most common DevOps activities: log analysis.
"""

# Bis mil Allah heer Rhaman nir Raheem

log_file = input("Enter The File Name: ") # app.log   # file to analyze it will bring from the same folder
output_file = "log_summary.txt"  # saves the results

"""
try: prevents program crash by handling errors safely.
with: Python automatically closes the file after use (safe).
open: Open(filename, mode, encoding) open file in required mode
readlines(): reads all lines into a list.

"""

try:
    with open(log_file, 'r', encoding="utf-8") as f: # refer to this opened file as f.
        lines = f.readlines()  # readlines() reads all lines from a file and stores them in a list.
except FileNotFoundError:
    print(f"ERROR: {log_file} not found.")
    exit("Please place a file in the folder or Check the Name of the file.")
# empty check list = []
if not lines:
    print(f"ERROR: {log_file} is empty.")
    exit("Without Data I am not able to do it.")

# Create a dictionary to store counts, count levels
counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for line in lines:
    if "INFO" in line:
        counts["INFO"] += 1   # increase count by 1, counts["INFO"] = counts["INFO"] + 1
    elif "WARNING" in line:
        counts["WARNING"] += 1
    elif "ERROR" in line:
        counts["ERROR"] += 1

# Create Summary(Report)
summary = (
    "Log Analysis Summary\n"
    "--------------------\n"
    f"Total lines: {len(lines)}\n"
    f"INFO: {counts['INFO']}\n"
    f"WARNING: {counts['WARNING']}\n"
    f"ERROR: {counts['ERROR']}\n"
)

# Print the Summary(Report)
print(summary)

# Now Writing

with open(output_file, "w", encoding="utf-8") as f:
    f.write(summary)

print(f"Saved summary to {output_file}")
exit("Happy Learning!!!")










