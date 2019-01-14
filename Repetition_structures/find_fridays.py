# Printing the date of the friday days in 2014 calendar
# ------------------------------------------------------

# Assume that the first day was 3rd of Jan
day = 3
month = 1
date = 0

# List of even months
even_months = [4, 6, 9, 11]

# Going through the calendar finding the fridays
for x in range(1, 13):
    for y in range(1, 32):

        if (x in even_months) and (y == 30):
            if day == y and x == month:
                print("{}.{}.".format(day, month))

                # Adding one week to the found day
                day += 7

            date = y
            break

        # February month
        elif x == 2 and y == 28:
            if day == y and x == month:
                print("{}.{}.".format(day, month))
                day += 7

            date = y
            break

        elif day == y and x == month:
            print("{}.{}.".format(day, month))
            day += 7

        date = y

    day = day - date
    month += 1
