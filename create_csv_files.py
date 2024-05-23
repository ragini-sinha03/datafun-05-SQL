import csv

# Define the filename
filename = "example.csv"

# Data to be written to the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 29, "Chicago"]
]

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")


