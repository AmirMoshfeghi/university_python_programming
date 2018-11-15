# Zip Boing program
# Every time the number is divisible by 3 the player has to say "zip"
# Every time the number is divisible by 7 the player has to say "boing"
# Also, if the number is divisible by both the numbers, the player should say "zip boing".

# Count starts from 1
count = 1

# How many times from input
limit = int(input("How many numbers would you like to have? "))

# Count until the limit specified by the user
while count <= limit:
    # Devidable by 3
    if count % 3 == 0:
        print("Zip")
        count += 1

    # Devidable by 7
    elif count % 7 == 0:
        print("Boeing")
        count += 1

    # Devidable by 3 and 7
    elif count % 21 == 0:
        print("Zip Boeing")
        count += 1
    # Otherwise print out number and go to next
    print(count)
    count += 1
