# oven_time_format.py
# Transforming the time format of measurement results and writing new data
# into a new file. The "ovendata.csv" file contains temperatures of three
# different ovens as the function of time, using Celsius grades.
# The time is in format hh:mm:ss. To make processing in Excel easier,
# the time measurement format must be changed from hh:mm:ss to mere seconds.

import os


def main():

    try:

        # Get the path of the file from user
        csv = str(input('Enter the full path\\filename.csv to open: '))
        time_file = open(csv, 'r')

        # Create a new file to write in the modified data
        csv_cpy = str(input('Enter the name of file to be written in: '))
        new = open(csv_cpy, 'w')

        # Print out the path of the created file
        print("The file is created in: " + os.getcwd())

        # Read the first line of the file
        line = time_file.readline()

        # Skip line if it is started with "Time"!!
        # Its the header line. Just copy it and go to next line
        if line.startswith("Time"):
            new.write(str(line))
            line = time_file.readline()

        # Go through all of the data
        while line != "":

            # Split each record and use the first part only
            record = line.split(";", 1)
            record[0] = to_sec(record[0])

            # write the modified data in new file
            new.write(record[0] + ";" + record[1])

            # Go to next line
            line = time_file.readline()

        # Close both files
        new.close()
        time_file.close()

    except (FileNotFoundError, PermissionError) as err:
        print(err)


# Function gets with format hh:mm:ss
# and returns it in seconds only
def to_sec(time_str):
    h, m, s = time_str.split(':')
    return str(int(h) * 3600 + int(m) * 60 + int(s))


main()
