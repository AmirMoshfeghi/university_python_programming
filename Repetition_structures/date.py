# The dates of the year
# Printing out the dates of the year in one column
# ___________________________________________________

# Going through the months and days
for x in range(1, 13):
    for y in range(1, 32):
        if x <= 7:
            if x == 2 and y == 29:
                break
            elif x % 2 == 0 and x != 2 and y == 31:
                break
            print("{}.{}".format(x, y))
        else:
            if x % 3 == 0 and y == 31 and x % 2 != 0:
                break
            print("{}.{}".format(x, y))

print("End")
