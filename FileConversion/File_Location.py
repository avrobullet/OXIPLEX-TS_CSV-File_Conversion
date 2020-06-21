class FileLocation():
    def __init__(self, filename, filename_location):
        self.filename = filename
        self.filename_location = filename_location
    # Check file location
    def checkLocation(self):
        # Check to make sure inputs are not blank
        if self.filename != "" and self.filename_location != "":
            # Go through each file location to verify
            print("\nChecking file location ", filename_location, "...")
            self.txtLocationValid()
        else:
            print("\nMissing user inputs...")

    # Validate if user input for the .txt file location is correct
    def txtLocationValid(self):
        # Try and catch the file error if there is nothing there
        try:
            file = open(self.filename_location + self.filename)
            print("File '", self.filename, "' detected...")
            file.close()
        except FileNotFoundError:
            print("Wrong file or file path...")

# Check if respective .txt and .csv locations exist
def fileCheck(filename, filename_location):
    file = FileLocation(filename, filename_location)
    file.checkLocation()
