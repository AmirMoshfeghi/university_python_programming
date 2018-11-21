# In this task, we create a simple driving simulation where the user drives
# through a two-dimensional desert surface, using a textual interface.
# The program calculates where the car moves and how much gas it uses.

MENU_TEXT = "1) Fill 2) Drive 3) Quit \n-> "
CAR_TEXT = "The tank contains {:.1f} liters of gas and " + \
           "the odometer shows {:.1f} kilometers."


class Car:

    def __init__(self, tank_size, gas_consumption, gas, odometer):

        # Car tank size and consumption (getting once from the user)
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption

        # amount of gas left in the car
        self.__gas = gas

        # Car's current odometer number
        self.__odometer = odometer

    def print_information(self):

        # Prints how much gas the car's tank contains and
        # what does the car's odometer show
        print(CAR_TEXT.format(self.__gas, self.__odometer))

    def capacity_check(self, refuel):

        # fills the tank by the specifies number gave by the user
        if refuel < 0:
            print('You cannot remove gas from the tank')
            return False
        elif (self.__tank_size < refuel) or \
                (self.__tank_size < (self.__gas + refuel)):
            print('Not allowed, the capacity of the tank is less')
            return False
        else:
            return True

    def fill(self, refuel):
        # Fills the tank
        self.__gas += refuel

    def drive(self, distance, gas_cons):

        # Indicates how many kilometers to drive
        if distance < 0:
            print('You can not go negative distance')
        else:
            self.__gas -= (distance * gas_cons)/100
            self.__odometer += distance


# The main function
def main():

    # What is the car's tank size and gas consumption
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers? ")

    gas = 0
    odometer = 0

    # Create an object from the Car class
    car = Car(tank_size, gas_consumption, gas, odometer)

    while True:

        # Print out car's current state
        car.print_information()

        # Pick a coice from the menu
        choice = input(MENU_TEXT)

        # Fill the tank
        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            if car.capacity_check(to_fill):
                car.fill(to_fill)

        # Drive with the car
        elif choice == "2":
            distance = read_number("How many kilometers to drive? ")
            car.drive(distance, gas_consumption)

        # EXIT - dont want to continue anymore
        elif choice == "3":
            break
    print("Thank you and bye!")


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


main()
