class csvFileEvaluation:
    # Imports
    import linecache as f_line
    import csv
    # Variables and objects
    next_line = True
    filename = ""
    num_counter = 0
    alpha_counter = 0
    data_line = 0
    title_line = 0
    columns = 0
    rows = 1
    titles = ["Raw Time","Time","Ox% A","[THC] A","[HBO] A", "[Hb] A","Ox% B","[THC] B","[HBO] B", "[Hb] B","Marker"]
    data = []

    # Determine which line is needed to start reading numerical data values from titles
    def checkLine(self, file):

        # Just make code that checks every line for the presence of a single char and print it
        for lines in file:
            line = lines[0]
            # Check for alphabet characters
            if 'a' <= line[0].lower() <= 'z':
                self.alpha_counter += 1
            # Check for numerical characters (when data starts)
            if '0' <= line[0] <= '9':
                self.num_counter += 1
            # Once there are two subsequent lines of data, break out of file reading
            if self.num_counter == 2:
                self.data_line = self.alpha_counter + 1
                self.title_line = self.alpha_counter
                break

        # Confirm the first line of data and the title
        print("Line with titles: ", self.title_line)
        print("First line with data: ", self.data_line)

        # Find the amount of columns to make
        data_content = self.f_line.getline(self.filename, self.data_line)
        csv_columns = data_content.split()
        while self.columns < len(csv_columns):
            self.columns += 1

    # Go to file line with the data and parse it into
    def dataAdd(self):
        # Return the line with content on it when linecache doesn't return a '' as an error
        data_to_parse = self.f_line.getline(self.filename, self.rows)

        # When linecache doesn't return a '' as an error it means there's no new data content
        if data_to_parse != '':
            self.data = data_to_parse.split()
            self.data_line += 1

            # Populate empty row cells with blank data
            z = 0
            while z <= self.columns:
                if len(self.data) < self.columns:
                    self.data.append("")
                z += 1

        # Inform that there is no more lines to be read once a '' error is set by linecachce
        else:
            self.next_line = False

    # Create .csv
    def createCSV(self, file, old_filename, new_filename):
        global csv
        self.filename = old_filename

        # Find the line (or row) that starts with data
        self.checkLine(file)

        # Write everything into the csv file!
        with open(new_filename, 'w') as csv_file:
            writer = self.csv.writer(csv_file)

            # Write information
            while self.next_line:
                # Find data to add to csv
                self.dataAdd()

                # Write column titles
                if self.rows == 3:
                    writer.writerow(self.titles)
                # Write data information
                else:
                    writer.writerow(self.data)

                self.rows += 1

        #Clear file cache
        self.f_line.clearcache()

# Start .csv conversion from .txt file "file_name"
def csvConversion(old_filepath, new_filepath):
    # Open and read txt file under variable "file"
    file = open(old_filepath, "r")
    csv = csvFileEvaluation()

    #Create csv with identified .txt file rows and columns
    csv.createCSV(file, old_filepath, new_filepath)

    #Print rows and columnes of "file"
    print("\nNew .csv file dimensions: ")
    print("Rows: ", csv.rows)
    print("Columns: ", csv.columns)

    # Close .txt file
    file.close()