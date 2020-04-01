from FileConversion import File_Location as file_location
from FileConversion import CSV_Conversion as csv_conversion
import re
import os

def main():
    print("Running V-0.2.3")
    fileOptions()

def fileOptions():
    # Select option for file "f"
    print("\nWhat would you like to do?")
    print("1. Convert a single graphdef.txt to .csv")
    print("2. Convert all graphdef.txt files to respective .csv files")
    print("3. Set time points for when experiment was run (once .csv file is created)")
    print("4. Run demo")

    # Identify options input by user is a numerical option
    file_option = input("\nEnter option: ")
    regex = re.findall("[1-4]", file_option)

    if regex:
        # Determine if the file and file path exists
        fileSelectPath(file_option)
        # Clear screen
        os.system('cls')
        fileCSVConversion()
    else:
        #Return to file options again to prompt user to select
        print("\nNo such option detected...")

# Create csv file based on user's selected location
def fileCSVConversion():
    global csv_file
    global all_txt_files

    # Find all graphdef.txt files and then convert them into their respective .csv files
    if txt_file == "graphdef.txt":
        for filename in os.listdir(txt_file_path):
            if re.search("graphdef.txt$", filename):
                csv_file = re.sub("txt", "csv", filename)
                csv_conversion.csvConversion(txt_file_path + filename, csv_file_path + csv_file)

    # Convert specific .txt file to csv
    else:
        # Convert txt_file nomenclenture into csv_file
        csv_file = re.sub("txt", "csv", txt_file)
        csv_conversion.csvConversion(txt_file_path + txt_file, csv_file_path + csv_file)

    # Get back to user options
    fileOptions()

# Check file path
def fileSelectPath(file_option):
    global txt_file
    global txt_file_path
    global csv_file_path

    # Prompt user for .txt file path, its name, and the new .csv file location
    if file_option == "1":
        txt_file = input("\nEntre name of the .txt file to be  converted: ")
        txt_file_path = input("Entre location of the .txt file: ")
        csv_file_path = input("Entre location for the newly made csv file: ")

    # Prompt user for the target folder with all the graphdef.txt files and set the new .csv folder
    elif file_option == "2":
        txt_file = "graphdef.txt"
        #txt_file_path = input("\nEntre location of the graphdef.txt files: ")
        #csv_file_path = input("Entre location for all the newly made .csv files: ")

    # Prompt user to set the time points for which the data is part of the experiment
    elif file_option == "3":
        time_1 = input("First time point :")
        time_2 = input("Second time point :")

    #Use default variables to test program capabilities
    elif file_option == "4":
        print("\nrunning demo...")

    # Check that .txt file location is valid
    file_location.fileCheck(txt_file, txt_file_path)

    # Return to user options
    fileOptions()

#Default Variables
txt_file = "00_demo_06-03-20_demo.txt"
csv_file = "00_demo_06-03-20_demo.csv"
txt_file_path = "/Users/alexanderdouglas/Desktop/Relaxation_Test_V1/"
csv_file_path = "/Users/alexanderdouglas/Desktop/"
file_options = [1,2,3]

if __name__ == "__main__":
    main()