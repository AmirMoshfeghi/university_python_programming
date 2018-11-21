# Working with Functions
# Making a house wine project
# Wine Temperature must be closely controlled at least most of the time.
# The program reads the temperature measurements of the wine container
# during the fermentation process and tells whether the wine is ruined or not.


def main():

    # Get number of measurements from the user
    number = int(input("Enter the number of measurements: "))

    # The entered number should not be negative or zero
    if number <= 0:
        print("The number of measurements must be a positive number.")

    # Check the status of the wine
    if check_temperature(number):
        print("Your wine is ready.")


def check_temperature(number):

    # count -> steps start from one,
    # alarm -> for checking if two numbers in a row are out in range,
    # per -> for count percentage
    count = 1
    alarm = 0
    per = 0

    # calculate 10% of total number of measurements
    percent = number * 0.1

    while count <= number:

        temp = int(input("Enter the temperature {}: ".format(count)))

        # Check if the measured number is in acceptable range
        if temp not in range(20, 26):
            alarm += 1
            per += 1
        else:
            alarm = 0

        # Go to next step
        count += 1

        # Wine is ruined if 2 measurements in a row
        # or 10% of total inputs are out of range
        if alarm == 2 or per > percent:
            print("The wine is ruined")
            break

    # if everything went fine
    else:
        return True


main()
