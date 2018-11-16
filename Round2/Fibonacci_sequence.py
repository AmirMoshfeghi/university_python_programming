# Fibonacci Series
# Printing out Fibonacci series based on the user input
# -----------------------------------------------------------------------

# How many times should the program count (number)
number = int(input("How many Fibonacci numbers do you want? "))

# Define variables
num_1 = 0
num_2 = 1
count = 0

# check if the input is valid
while number <= 0:
    print("The input is not valid, please enter a positive (integer) number")

if number == 1:
    print("Fibonacci sequence to {}: ".format(number))
    print(num_1)

# start to calculate Fibonacci
else:
    print("Fibonacci sequence to {}: ".format(number))
    while count < number:
        print(num_1, end=' ')
        temp = num_1 + num_2

        # exchanging the values (going step by step further)
        num_1 = num_2
        num_2 = temp
        # go to the next sequence
        count += 1
