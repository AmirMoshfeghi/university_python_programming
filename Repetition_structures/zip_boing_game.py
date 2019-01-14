# Zip Boing program
# Every time the number is divisible by 3 the player has to say "zip"
# Every time the number is divisible by 7 the player has to say "boing"
# Also, if divisible by both the numbers, the player should say "zip boing"

# Count starts from 1
count = 1

# How many times from input
limit = int(input("How many numbers would you like to have? "))

# Count until the limit specified by the user
while count <= limit:

    # Dividable by 3 and 7
    if count % 21 == 0:
        print("zip boing")

    # Dividable by 3
    elif count % 3 == 0:
        print("zip")

    # Dividable by 7
    elif count % 7 == 0:
        print("boing")

    # Otherwise print out number
    else:
        print(count)

    count += 1
