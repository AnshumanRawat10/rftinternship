# Given logs
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters
error_count = 0
info_count = 0
warning_count = 0

# Loop through logs
for log in logs:
    log = log.upper()  # ignore case sensitivity

    if "ERROR" in log:
        error_count += 1
    elif "INFO" in log:
        info_count += 1
    elif "WARNING" in log:
        warning_count += 1

# Store counts in dictionary
log_counts = {
    "ERROR": error_count,
    "INFO": info_count,
    "WARNING": warning_count
}

# Find most frequent log type
most_frequent = max(log_counts, key=log_counts.get)

# Output
print("Log Counts:")
print("ERROR:", error_count)
print("INFO:", info_count)
print("WARNING:", warning_count)

print("\nMost Frequent Log Type:", most_frequent)