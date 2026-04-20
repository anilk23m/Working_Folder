import csv
with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_name", "status", "duration"])
    writer.writerow(["test_login", "PASS", 1.2])
    writer.writerow(["test_search", "FAIL", 2.2])
    writer.writerow(["test_checkout", "FAIL", 3.2])

with open("result.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0], row[1], row[2])
with open("result.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["test_name"], row["status"], row["duration"])


