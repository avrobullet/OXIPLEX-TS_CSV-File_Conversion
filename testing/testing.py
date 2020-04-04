# # Open and read from file # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def fileOpen():
    # Try and catch the file error if there is nothing there
    try:
        file = open("demofile.txt")
    except FileNotFoundError:
        print("Wrong file or file path...")
        print("Creating file 'demofile.txt'...")
        file = open('demofile.txt', "x")
        file.close()
    # Presence of file "f" detected
    else:
        print("File 'demofile.txt' detected...")

    # Read first few lines of from the file
    firstline = file.readline()
    #file.seek(0)
    firstline_1 = file.readline(1)
    #file.seek(0)
    firstline_2 = file.readline(2)
    #file.seek(0)
    firstline_3 = file.readline(3)
    file.seek(0)

    print("Firstline (all): ", firstline, "\n",
          "Firstline (0):   ", firstline_1, "\n",
          "Firstline (1):   ", firstline_2, "\n",
          "Firstline (2):   ", firstline_3)

    for lines in file:
        line = lines[0]
        # Check for alphabet characters
        if 'a' <= line[0].lower() <= 'z':
            print("It's a letter: ",line)
        # Check for numerical characters (when data starts)
        if '0' <= line[0] <= '9':
            print("It's a number: ", line)

    #Close file "f" before being opened with different options
    file.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Character comparisons between numeric and alphabet characters # #
def checkLine():
    global alpha_counter
    global num_counter
    global data_line
    global title_line
    global file
    global f_line
    global columns

    # Just make code that checks every line for the presence of a single char and print it
    for lines in file:
        line = lines[0]
        # Check for alphabet characters
        if 'a' <= line[0].lower() <= 'z':
            alpha_counter += 1
            print("It's a letter: ",line)
        # Check for numerical characters (when data starts)
        if '0' <= line[0] <= '9':
            num_counter += 1
            print("It's a number: ", line)
        # Once there are two subsequent lines of data, break out of file reading
        if num_counter == 2:
            data_line = alpha_counter + 1
            title_line = alpha_counter
            break

    # Confirm the first line of data and the title
    print("First line with data: ", data_line)
    print("Line with titles: ", title_line)

    # Find the amount of columns to make
    data_content = f_line.getline(filename, data_line)
    titles = data_content.split()
    while columns < len(titles):
        print(columns)
        columns += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Go to file line with the titles and separate into csv# # # # # # # # # # # # # # # # #
def titleAdd():
    global title_line
    global titles
    global f_line
    global columns

    #Just hardcode the titles...
    title_to_parse = f_line.getline(filename, title_line)
    print('\nThis is the line with the title names: ', title_to_parse)

    # Create titles by parsing its characters "char" into distinct words "word"
    word = ""
    for char in title_to_parse:
        if char != " ":
            word += char
            print(word)
        elif char == " ":
            try:
                if char == " ":
                    print("Found the next keyword")
                    titles.append(word)
                    # Reset word to being blank
                    word = ""
            except IndexError:
                print("No more words found in file name")
                titles.append(word)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Go to file line with the data and parse it into # # # # # # # # # # # # # # # # #
def dataAdd():
    global data_line
    global data
    global f_line
    global next_line
    global columns

    # Return the line with data content on it
    data_to_parse = f_line.getline(filename, data_line)

    # When linecache doesn't return a '' as an error it means there's no new data content
    if data_to_parse.strip() != '':
        print('\nThis is the line with the data: ', data_to_parse)
        data = data_to_parse.split()
        data_line += 1

        # Populate empty row cells with blank data
        z = 0
        while z <= columns:
            if len(data) < columns:
                data.append("")
            z += 1

    # Inform that there is no more lines to be read once a '' error is set by linecachce
    else:
        next_line = False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Create csv from title and data lists # # # # # # # # # # # # # #
def createCSV():
    global titles
    global data
    global next_line
    global file
    file_destination = r'C:\Users\Alex\PycharmProjects\OXIPLEX-TS_CSV-File_Conversion\testing\00_demo_06-03-20_demo_graphdef.csv'
    #Add titles
    #titleAdd()

    # Write everything into the csv file!
    with open(file_destination, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(titles)

        #Check for data
        while next_line:
            writer.writerow(data)
            dataAdd()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Test calling modulues, classes, and functions from other subdirectories # # # # # # # # # # # # # #
def subdirCalls():
    tp.initiateTimePoints()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Variables and modules
import linecache as f_line
import csv
from DataUsage import Time_Points as tp

next_line = True
num_counter = 0
alpha_counter = 0
data_line = 0
title_line = 0
columns = 0
titles = ["Raw Time","Time","Ox% A","[THC] A","[HBO] A", "[Hb] A","Ox% B","[THC] B","[HBO] B", "[Hb] B","Marker"]
data = []
filename = r'C:\Users\Alex\PycharmProjects\OXIPLEX-TS_CSV-File_Conversion\testing\00_demo_06-03-20_demo.txt'
file = open(filename)

# Function calling
fileOpen()
checkLine()
#titleAdd()
#dataAdd()
createCSV()
subdirCalls()

#Clean up
f_line.clearcache()
file.close()

def runTests():
    print("Testing")