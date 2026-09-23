from datetime import datetime

# Converts a weight from pounds to kilograms.
def convertData(weight):
    return weight / 2.205


# Inserts comma-separated data into the ZooData.csv file.
def insertData(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
        return True
    except Exception as error:
        print("Error writing to file:", error)
        return False


# Displays the contents of the ZooData.csv file.
def viewData(file_path):
    try:
        print("The file", file_path)

        with open(file_path, "r") as file:
            print(file.read())
    except Exception as error:
        print("Error reading file:", error)


# Gets weight data from the user, converts it, and saves it to the CSV file.
def getInput():
    entries = int(input("How many entries are you inputting? "))

    for entry in range(entries):
        date = input("Enter a date: ")
        weight = float(input("Enter the weight in pounds for the inputted date: "))

        # Calls convertData with weight as the argument and returns the converted weight in kilograms.
        converted_weight = convertData(weight)

        data = str(date) + "," + str(weight) + "," + str(converted_weight)

        try:
            if insertData("ZooData.csv", data):
                print("The following data was saved at", datetime.now())
                print(data)
                print()
        except Exception as error:
            print("Error saving data:", error)


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
elif choice == "2":
    print("You selected", choice, "at", datetime.now())
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")