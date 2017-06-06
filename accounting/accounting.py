# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('items.csv')

    option = ""
    while option != "0":
        handle_menu()
        try:
            option = choose(table)
        except KeyError as err:
            ui.print_error_message(err)


def handle_menu():
    
    menu_name = 'Accounting Manager:'
    menu_options = ['Show records', 'Add a record',
                    'Remove a record', 'Update a record',
                    'Most profitable year', 'Average profit per item']

    ui.print_menu(menu_name, menu_options, 'Exit to menu')


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        ui.get_inputs(list_labels, 'Which record would you like to remove?'
        remove(table, id_)
    elif option == "4":
        ui.get_inputs(list_labels, title)
        update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        ui.get_inputs(list_labels, title)
        avg_amount(table, year)
    else:
        raise KeyError("There is no such option.")
    return option


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
