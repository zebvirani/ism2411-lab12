#1. python makes it easier to calculate and automate without doing everythijng manually
#2.a convience store could use it to update daily sales and revenue. it works by adding new info and makes it easier to see history
 

import csv
from datetime import datetime
file_path = "data/sales.csv"

#exercise1and2 kinda
with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#exercise3
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
    
#exercise4
total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: {total_revenue:.2f}")

#exercise5
original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_count += 1

print("Original rows:", original_count)
print("Cleaned rows:", cleaned_count)

#exercise6
dict_total = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader Total: ${dict_total:.2f}")
#reader is better when you know the order of the columns so you can use indexs
#dict reader is better when you know the names of the categories

#exercise7
sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

#exercise8
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{current_time} - Total Revenue: ${total_revenue:.2f}")

print("log updated")