# GLobal Variables
import re as reggie

class TimeConversion():
    # Initialization
    def __init__(self, user_input=None):
        # Class Variables
        self.time_formats = [24, 60, 60, 1000]  # In order: hours=24; minutes=60; seconds=60; miliseconds=1000
        self.time_converted = {'hours': 00, 'minutes': 00, 'seconds': 00, 'miliseconds': 00}
        self.raw_time = 0 # For unit test purposes (see
        self.input = user_input

        # In the event of a unit test
        try:
            self.raw_time = int(self.input)
        except ValueError:
            if self.input == 'unit test':
                self.timeFormalFormat(9145890)  # Convert designated 9145890 miliseconds to 2hours:32minutes:25seconds:889Ms
                self.display('Unit test Class TimeConversion!')  # Determine if conversion works
            else:
                print('Invalid Request!')

    # Converting milisecond times into HH:MM:SS:MsMs format
    def timeFormalFormat(self, new_raw_time=None):
        # In the event that the submitted raw time was incorrect and needs to be replaced
        if new_raw_time != None: self.raw_time = new_raw_time

        # Set a temporary variable (converted to hours for further processing)
        tempt_time = str((1 / self.time_formats[1]) \
                         * (1 / self.time_formats[2]) \
                         * (1 / self.time_formats[3]) \
                         * self.raw_time)

        # Split, calculate, and save formatted time stamps (hours, minutes, seconds, miliseconds
        iterate = 0
        for key in self.time_converted.keys():
            if iterate == 0:
                self.time_converted[key], next_tempt_time = reggie.split("[.]", tempt_time)
            elif iterate > 0:
                tempt_time = str(float('0.' + next_tempt_time) * self.time_formats[iterate])
                self.time_converted[key],next_tempt_time = reggie.split("[.]", tempt_time)
            iterate+=1

    # Converting HH:MM:SS:MsMs time into miliseconds
    def milisecondRawFormat(self, new_raw_time=None):
        pass

    # Display converted time
    def display(self, quote=None):
        # What called for a unit test, have the user check that the calculations match the expected result
        if quote != None:
            print(quote)
            print('--> Knowing that {} miliseconds is: 2 hours 32 minutes 25 seconds 889 miliseconds'.format(self.raw_time))
            print('--> The calculations should matche it:   ', end='')
        else:
            print('Current time:', end=' ')

        for key,value in self.time_converted.items():
            print(value,key, end=' ')

user_input = input("Enter raw time:")
convert_time = TimeConversion(user_input)
try:
    if convert_time.input != 'unit test':
        if int(convert_time.input):
            convert_time.timeFormalFormat()
            convert_time.display()
except ValueError:
    pass
