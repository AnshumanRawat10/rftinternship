# Read CSV file
with open("sales.csv", "r") as file:
    lines = file.readlines()

# Extract headers
headers = lines[0].strip().split(",")

data = []

# Convert CSV rows into list of dictionaries
for line in lines[1:]:
    values = line.strip().split(",")

    record = {
        "PRODUCT": values[0].strip(),
        "QUANTITY": int(values[1]),
        "PRICE": int(values[2])
    }

    # BONUS: Add TOTAL column
    record["TOTAL"] = record["QUANTITY"] * record["PRICE"]

    data.append(record)

# Calculate total sales per product
product_sales = {}

for record in data:
    product = record["PRODUCT"]
    total = record["TOTAL"]

    if product in product_sales:
        product_sales[product] += total
    else:
        product_sales[product] = total

# Calculate total revenue
total_revenue = sum(product_sales.values())

# Find top-selling product
top_product = max(product_sales, key=product_sales.get)

# Sort products by revenue (descending)
sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

# Output
print("Data with TOTAL column:")
for record in data:
    print(record)

print("\nTotal Sales per Product:")
for product, revenue in product_sales.items():
    print(product, ":", revenue)

print("\nTotal Revenue:", total_revenue)
print("Top-Selling Product:", top_product)

print("\nSorted by Revenue:")
for product, revenue in sorted_sales:
    print(product, ":", revenue)