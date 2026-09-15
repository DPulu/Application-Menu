from datetime import datetime

def convertData(weight):
    return weight / 2.205


def getInput():
    entries = int(input("How many entries are you inputting? "))

    for entry in range(entries):
        date = input("Enter a date: ")
        weight = float(input("Enter the weight in pounds for the inputted date: "))

        # Calls convertData with weight as the argument and returns the converted weight in kilograms.
        converted_weight = convertData(weight)

        print("The following was saved at", datetime.now(), ":")
        print(date, weight, converted_weight)
        print()


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

if choice == "1":
    print("You selected", choice, "at", datetime.now())
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")