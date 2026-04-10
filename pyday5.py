# Open and read CSV file
file = open("data.csv", "r")

lines = file.readlines()   # read all lines
file.close()

# Extract headers
headers = lines[0].strip().split(",")

data = []   # list to store dictionaries

# Process each row
for line in lines[1:]:
    values = line.strip().split(",")
    
    record = {}
    
    for i in range(len(headers)):
        key = headers[i]
        value = values[i] if i < len(values) else ""   # handle missing values
        
        # Convert numbers to int if possible
        if value.isdigit():
            value = int(value)
        
        record[key] = value
    
    data.append(record)

# Print structured data
print("Data:", data)

# Bonus: Calculate average marks
total = 0
count = 0

for record in data:
    if "MARKS" in record and isinstance(record["MARKS"], int):
        total += record["MARKS"]
        count += 1

average = total / count if count > 0 else 0

print("Average Marks:", average)