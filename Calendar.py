# """
# Codecademy Project - Learn Python 2
# Command Line Calendar
# Nasim Ahmed
# """

# import sleep and strftime
from time import sleep, strftime

# store user's name in constant variable
USER_NAME = "Nasim"

# create calendar dictionary
calendar = {}


def welcome():
    print("Welcome " + USER_NAME + ".")
    print("Calendar Opening...")
    sleep(1)
    # print date and time using strftime
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("The time is: " + strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")


def start_calendar():
    # greet user
    welcome()
    # add while loop that uses start as boolean condition
    start = True
    while start:
        # prompt user to enter action
        user_choice = input(
            "A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        # convert user choice to uppercase
        user_choice = user_choice.upper()
        # check what the user's choice was
        if user_choice == "V":
            # check if calendar is empty
            if len(calendar.keys()) < 1:
                print("Calendar is empty")
            else:
                print(calendar)
        elif user_choice == "U":
            # prompt user to choose date and enter update
            date = input("What date? ")
            update = input("Enter update: ")
            # add update to specified date in calendar
            calendar[date] = update
            print("Calendar updated.")
            print(calendar)
        elif user_choice == "A":
            # prompt user to enter event and choose date
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            # check if date format is correct
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("Invalid date entered")
                # check if user wants to try again
                try_again = input("Try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    # use continue to start loop from beginning
                    continue
                else:
                    # set start to false to exit loop and quit program
                    start = False
            else:
                # add event to specified date in calendar
                calendar[date] = event
                print("Event Added.")
                print(calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("Calendar is empty")
            else:
                # prompt user for event to delete
                event = input("What event?")
                # search for date by iterating through keys using for loop
                for date in calendar.keys():
                    # check if event exists
                    if event == calendar[date]:
                        del calendar[date]
                        print("Event Deleted.")
                        print(calendar)
                    else:
                        print("Event does not exist")
        elif user_choice == "X":
            # exit program by changing start to false
            print("Goodbye...")
            start = False
        else:
            print("Invalid choice. Terminating program...")
            start = False


# call start_calendar() to start program
start_calendar()
