# Variables
import re as reggie
class TimeConversion():
    # Initialization
    def __init__(self, raw_time=None):
        self.raw_time = raw_time
        self.time_formats = {'hours': 24, 'minutes': 60, 'seconds': 60, 'miliseconds': 1000}
        self.time_converted = {'hours': 00, 'minutes': 00, 'seconds': 00, 'miliseconds': 00}
    # Converting raw times into their respective (and readable) formats
    def timeConversion(self, new_raw_time=None):
        # In the event that the submitted raw time was incorret and needs to be replaced
        if new_raw_time != None: self.raw_time = new_raw_time

        # Set a temporary variable
        tempt_time = str((1 / self.time_formats['minutes']) \
                         * (1 / self.time_formats['seconds']) \
                         * (1 / self.time_formats['miliseconds']) \
                         * self.raw_time)

        # Split to save formatted hours
        hours, minutes = reggie.split("[.]", tempt_time)
        self.time_converted['hours'] = hours
        minutes = '0.' + minutes

        # Calculate and split to convert and save minutes
        tempt_time = str(float(minutes) * self.time_formats['minutes'])
        minutes, seconds = reggie.split("[.]", tempt_time)
        self.time_converted['minutes'] = minutes
        seconds = '0.' + seconds

        # Calculate and split to convert and save seconds
        tempt_time = str(float(seconds) * self.time_formats['seconds'])
        seconds, miliseconds = reggie.split("[.]", tempt_time)
        self.time_converted['seconds'] = seconds
        miliseconds = '0.' + miliseconds

        # Calculate and split to convert and save minutes
        tempt_time = str(float(miliseconds) * self.time_formats['miliseconds'])
        miliseconds, _ = reggie.split("[.]", tempt_time)
        self.time_converted['miliseconds'] = miliseconds

    # Display converted time
    def timeDisplay(self):
        print('Current time:', end=' ')
        for times in self.time_converted:
            print(self.time_converted[times], times, end=' ')

entered_time = int(input("Enter raw time:"))
convert_time = TimeConversion(entered_time)
convert_time.timeConversion()
convert_time.timeDisplay()
