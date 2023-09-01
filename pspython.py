import sys
from tabulate import tabulate

def load_csv_data(filename, delimiter=','):
    lines = []
    try:
        with open(filename) as file:
            for line in file:
                line = line.strip()
                if line:
                    lines.append(line.split(delimiter))
    except FileNotFoundError:
        sys.exit(f"File '{filename}' doesn't exist")  # Improved error message for FileNotFoundError

    return lines

def sort_data(data, column):
    if column >= len(data[0]):
        print("Invalid column index for sorting")  # Notify if the column index is invalid
        return data

    return [data[0]] + sorted(data[1:], key=lambda x: x[column])

def filter_data(data, column, value):
    if column >= len(data[0]):
        print("Invalid column index for filtering")  # Notify if the column index is invalid
        return data

    filtered = [data[0]]
    for row in data[1:]:
        if row[column].strip() == value:
            filtered.append(row)

    return filtered

# Specify the CSV filename here
filename = "airtravel.csv"  # Replace with your CSV file's name

try:
    lines = load_csv_data(filename)
except Exception as e:
    sys.exit(f"Error loading data: {e}")  # Improved error message for loading data

print(tabulate(lines, headers="firstrow", tablefmt="grid"))

while True:
    choice = input("\nDo you want to:\n"
                   "1. Sort data\n"
                   "2. Filter data\n"
                   "3. Exit\n"
                   "Enter your choice: ")

    if choice == '1':
        column = int(input("Enter the column index to sort by: "))
        lines = sort_data(lines, column)
        print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    elif choice == '2':
        column = int(input("Enter the column index to filter by: "))
        value = input("Enter the value to filter for: ")
        lines = filter_data(lines, column, value)
        print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    elif choice == '3':
        sys.exit("Exiting the program")  # Exiting the program with a notification

    else:
        print("Invalid choice. Please choose again.")