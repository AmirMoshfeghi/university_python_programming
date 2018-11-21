# The program requests a number from the user and then prints out
# its binary representation.
# The program does not use a format string.
# _________________________________________________________________

# Printout a list, containing the powers 1-32768
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

# receive a number from the user
num = int(input("Please enter a number: "))

# deleting the 0's before the last 1
# example: 00010111 -> 10111
printing = False

for power in powers:
    bit = num // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    num %= power
