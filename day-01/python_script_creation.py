# https://chatgpt.com/share/695f47b7-ccb8-8002-85f2-4ead53e49923
# Takes threshold values (CPU, disk, memory) from user input
# Also fetches system metrics using a Python library (example: psutil)
# Compares metrics against thresholds
# Prints the result to the terminal

import psutil

# Get Threshold Valus from a User

cpu_threshold = float(input("Enter CPU usage threshold (%): "))
memory_threshold = float(input("Enter memory usage threshold (%): "))
disk_threshold = float(input("Enter disk usage threshold (%): "))

# Fetch current system_metrics

cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current cpu usage: {cpu_usage}")
memory_usage = psutil.virtual_memory().percent
print(f"Current memory usage: {memory_usage}")
disk_usage = psutil.disk_usage('/').percent
print(f"Current disk usage: {disk_usage}")

# Compare usage against threshold and print results.

# Compare CPU
if cpu_usage > cpu_threshold:
    print("[ALERT] CPU usage is HIGH")
else:
    print("[OK] CPU usage is normal")

# Compare Memory
if memory_usage > memory_threshold:
    print("[ALERT] Memory usage is HIGH")
else:
    print("[OK] Memory usage is normal")

# Compare Disk
if disk_usage > disk_threshold:
    print("[ALERT] Disk usage is HIGH")
else:
    print("[OK] Disk usage is normal")
