from datetime import datetime

print("Duspul5115 Spreadsheet Automation Menu")

menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

print("Choose a number from the following options")

for option in menu_options:
    print(option)

choice = input("Enter your selection: ")

if choice == "1" or choice == "2" or choice == "3":
    print("You selected", choice, "at", datetime.now())
else:
    print("Error: Invalid choice selected.")