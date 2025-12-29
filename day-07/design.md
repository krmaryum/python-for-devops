# Day 07 – Thinking Before Coding (DevOps Mindset)

## Script Name
System Resource Monitoring Script

---

## What problem am I solving?

- Manually checking CPU, memory, and disk usage on a system takes time.
- High resource usage can go unnoticed and may cause performance issues or system crashes.
- There is a need for a simple script that checks system health and alerts when usage is too high.

---

## What input does my script need?

- User provides threshold values for:
  - CPU usage percentage
  - Memory usage percentage
  - Disk usage percentage

- Input format:
  - Numeric values (float)
  - Example:
    - CPU threshold: 75
    - Memory threshold: 80
    - Disk threshold: 85

- Assumptions:
  - User enters valid numeric values
  - `psutil` library is installed
  - Script runs on a local system

---

## What output should my script give?

- Output type:
  - Terminal / console output

- Output includes:
  - Current CPU usage
  - Current memory usage
  - Current disk usage

- Status messages:
  - `[ALERT]` if usage exceeds the threshold
  - `[OK]` if usage is within the threshold

---
- Example output:

## What are the main steps involved?

1. Take CPU, memory, and disk threshold values from the user
2. Fetch current CPU usage using `psutil`
3. Fetch current memory usage using `psutil`
4. Fetch current disk usage using `psutil`
5. Display current usage values in the terminal
6. Compare each resource usage with its threshold
7. Print `[ALERT]` or `[OK]` messages based on the comparison

---

## Possible edge cases

- User enters invalid or non-numeric input
- `psutil` library is not installed
- Disk path may differ on some systems
- Script needs to be executed repeatedly for monitoring

---

## DevOps perspective / Future improvements

- Can be scheduled using a cron job for continuous monitoring
- Can be extended to send alerts via email or Slack
- Can log results to a file for auditing and analysis
- Can read threshold values from a configuration file instead of user input
