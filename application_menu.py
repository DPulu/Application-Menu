from datetime import datetime

print("Duspul5115 Spreadsheet Automation Menu")
print("Choose a number from the following options:")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores it into the variable called choice.
choice = input("Enter your selection: ")

print("You selected", choice, "at", datetime.now())