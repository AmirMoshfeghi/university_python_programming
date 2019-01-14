# Print out each date of the year in one column

# going through the months and days
for x in range(1, 13):
    for y in range(1, 32):

        # first half of the year (#7 = July)
        if x <= 7:

            # odd months are 31 days, February (x=2) is an exception
            if (x % 2 == 0 and y == 31) or (x == 2 and y == 29):
                break

            # print out the dates
            print("{}.{}.".format(y, x))

        # second half of the year
        else:
            if x % 2 != 0 and y == 31:
                break

            print("{}.{}.".format(y, x))
