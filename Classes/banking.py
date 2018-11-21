# Bank account project
# The programm allowing us to have a starting balance, make deposits,
# make withdrawals, and get the current balance.

# Menu for multichoice
MENU_TEXT = "Please choose one option:\n" \
            "1)Deposit 2)Withdraw 3)Show balance 4)Exit \n"


# The Bank class represents users name and bank account details
class Bank:

    # The method accepts arguments users input and initializes each of them.
    # The arguments are users name and starting balance.
    def __init__(self, name, start_bal):

        self.__name = name
        self.__sBal = start_bal

    # Function to deposit the amount of money entered by user
    def add_balance(self, deposit):
        self.__sBal += deposit

    # Function to withdraw the requested amount by the user
    def withdraw(self, amount):

        # Check if the entered amount is more than the users deposit or not
        if self.__sBal >= amount:
            self.__sBal -= amount
        else:
            # Printout Error if the user does not have enough money
            print('Error, no enough money')

    # Return username
    def username(self):
        return self.__name

    # Return the balance of user
    def get_balance(self):
        return self.__sBal


# Main function
def main():

    try:
        # Name of the user
        name = input("Please enter your name: ")

        # User's starting balance
        start_bal = float(input("Please enter your starting balance: "))

        # Create an object from the class
        saving = Bank(name, start_bal)

        while True:
            choice = input(MENU_TEXT)

            # To deposit
            if choice == "1":
                # How much the user wants to deposit
                deposit = float(input("How much do you want to deposit: "))
                saving.add_balance(deposit)

            # Withdraw money
            if choice == "2":
                amount = float(input("How much would you like to withdraw? "))
                saving.withdraw(amount)

            # Show current balance
            if choice == "3":
                print("Your account balance is ${}\n".format(saving.get_balance()))

            # Exit
            if choice == "4":
                print("See you again {}".format(saving.username()))
                break

            # Print the current balance
            print("Your account balance is ${}\n".format(saving.get_balance()))

    # ValueErrors during inputs
    except ValueError:
        print("Please enter a number")


main()
