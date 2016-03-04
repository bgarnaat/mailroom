"""Mailroom Module."""

import sys
DONORS = {'Ben': [0, 0]}

def start():
    """Print welcome message."""


def get_user_input():
    """Return user input."""
    valid = False
    while not valid:
        print("Welcome to Mailroom Madness! Please choose from the following:\n"
    " T - Send a (T)hank you\n R - Create a (R)eport\n Q - (Q)uit the program")
        user_input = input('> ').lower()
        valid = validate_user_input(user_input)
    return user_input


def validate_user_input(user_input):
    """Return whether or not user_input is valid."""
    responses = ['t', 'r', 'q']
    return user_input in responses


def handle_user_input(user_input):
    """Return user input."""
    if user_input == 't':
        thank_you()
        valid = True
    elif user_input == 'r':
        create_report()
        valid = True
    elif user_input == 'q':
        sys.exit()


def thank_you():
    """Add donation for a donor  print thank you email."""
    donor = get_donor()
    donation = get_donation()
    add_donation(donor, donation, DONORS)
    display_email(donor, donation)
    get_user_input()


def display_list():
    """Display donor list."""
    for key in DONORS:
        print(key)


def add_donation(donor, donation_amount, donor_dict):
    donor_dict.setdefault(donor, []).append(donation_amount)


def get_donor():
    """Return list of donations for given donor."""
    print("Type 'list' for the donor list or enter donor name.")
    user_input = input('> ').lower()
    while user_input == 'list':
        display_list()
        print("Type 'list' for the donor list or enter donor name.")
        user_input = input('> ').lower()
    return user_input





def display_email(donor, donation_amount):
    """Print email with donor name and donation amount."""
    print("Dear {},\n Thank you for your generous donation of ${}. "
        "We here at the Seattle Toaster Enthusiasts Association "
        "will use the money to fund our annual pilgrimage to "
        "Stanley North Dakota, the toaster mecca of the midwest.\n"
        "Thank you very much,\n Margie Plumwhistle, President S.T.E.A".format(donor, donation_amount))


if __name__ == '__main__':
    # main()

    user_input = get_user_input()
    handle_user_input(user_input)
