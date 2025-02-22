from account_class import Account
from csv_read_write import save_accounts_to_csv
import csv


# function to pull up account creation screen
def create_account(accounts):
    username_ = " "
    password_ = " "

    # following code checks if there are 5 stored passwords already
    line_count = len(accounts)
    if line_count >= 5:
        print("All permitted accounts have been created, please come back later")
        return

    # following code allows user to create a username and validates that it is unique
    print("Enter the username you wish to use:")

    username_condition = True
    while username_condition:  # while loop allows user to keep entering until input is valid
        exit_loop = False
        username_ = input()

        for x in accounts:
            if username_ == x.username:
                print("Error: entered username is taken. enter another username")
                exit_loop = True
                break

        if not exit_loop:
            username_condition = False

    # following code allows user to create a password and validates input with the given conditions
    print("Enter the password you wish to use. Your password must contain: \n",
          "a minimum of 8 characters\n",
          "a maximum of 12 characters\n",
          "at least one capital letter\n",
          "at least one digit\n",
          "at least one non-alphabetic character")

    password_secure = False
    while not password_secure:  # while loop allows user to keep entering until input is valid
        password_ = input()
        password_secure, message = is_secure(password_)
        if not password_secure:
            print(message)

    # following code allows the user to save their first and last name
    print("Enter your first name:")
    firstname_ = input()

    print("Enter your last name: ")
    lastname_ = input()

    # following code creates an account object for the newly created account
    created_account_ = Account(username_, password_, firstname_, lastname_)
    accounts.append(created_account_)

    # write the accounts to the csv
    save_accounts_to_csv(accounts)

    print("You've Successfully created an account!\n")


# Function to check if a password is secure, a secure password should contain
# minimum of 8 characters, maximum of 12 characters, at least one capital letter, one
# digit, one non-alpha character
def is_secure(passwd):
    if not 8 <= len(passwd) <= 12:
        return False, 'Error: password must be a minimum of 8 and a maximum of 12 characters'
    contain_capital = False
    contain_digit = False
    contain_non_alpha = False
    for c in passwd:
        # check if c is a capital letter
        if c.isalpha() and c.upper() == c:
            contain_capital = True
        # check if c is a digit
        if c.isdigit():
            contain_digit = True
        # check if c is a non-alpha character
        if not c.isalpha():
            contain_non_alpha = True
    if not contain_digit:
        return False, "Error: password must contain at least 1 digit"
    if not contain_capital:
        return False, "Error: password must contain at least 1 capital letter"
    if not contain_non_alpha:
        return False, "Error: password must contain at least 1 non-alpha character"
    return True, ''
