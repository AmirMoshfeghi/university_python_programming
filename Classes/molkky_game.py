# Scoring for Mölkky
# Mölkky is a Finnish game where players aim to score exactly 50 points.
# If a player ends up having more than 50 points, his/her score will be
# decreased to 25 points.
# ________________________________________________________________________

# Constant values for the Max and Min points
MAX = 50
MIN = 25


# The Player class represents the player his/her points and round
class Player:

    # Initialize the attributes
    def __init__(self, player):
        self.__player = player
        self.__point = 0
        self.__round = 0

    # Return player name
    def get_name(self):
        return self.__player

    # Calculates the players points
    def add_points(self, points):
        self.__point += points
        self.__round += 1
        if float(self.__point / self.__round) < points:
            print('Cheers {}!'.format(self.__player))

    # function Specifies who has won the game
    def has_won(self):

        # if the point is higher than 50, set the point to 25
        if self.__point > MAX:
            self.__point = MIN
            print('{} gets penalty points!'.format(self.__player))

        # if players point is between 40 and 50 a notice will be displayed
        elif self.__point in range(40, MAX):
            print("{} needs only {} points. It's better to avoid knocking"
                  " down the pins with higher points.".format(self.__player, MAX - self.__point))

        # situation that the player has won the game
        elif self.__point == MAX:
            return True

    # return the player point
    def get_points(self):
        return self.__point


# Main function
def main():

    # Create 2 variables which are the objects initiated from the class Player
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # Changing the turn between players
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        # Get the number from the player
        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        # adding the points for each player
        in_turn.add_points(pts)

        # check the win status for the current player
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")

        # Print status and each player's score
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p")
        print(player2.get_name() + ":", player2.get_points(), "p")

        print("")

        # next throw
        throw += 1


main()
