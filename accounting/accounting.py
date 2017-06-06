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
    table = data_manager.get_table_from_file('accounting/items.csv')

    option = ""
    while option != "0":
        handle_menu()
        try:
            table, option = choose(table)
        except KeyError as err:
            ui.print_error_message(err)
    data_manager.write_table_to_file("accounting/items.csv", table)


def handle_menu():

    menu_name = 'Accounting Manager:'
    menu_options = ['Show records', 'Add a record',
                    'Remove a record', 'Update a record',
                    'Most profitable year', 'Average profit per item']

    ui.print_menu(menu_name, menu_options, 'Exit to menu')


def choose(table):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
    elif option == "3":
        id_ = ui.get_inputs(['ID: '], 'Which record would you like to remove?')
        table = remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(['ID: '], 'Which record would you like to update?')
        table = update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        year = ui.get_inputs(['Year: '], 'Average profit per item in given year.')
        avg_amount(table, year)

    return table, option


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

    data_names = ['month', 'day', 'year', 'type (in/out)', 'amount']

    inputs = ui.get_inputs(data_names, 'Adding new record:')

    id_ = common.generate_random(table)
    inputs.insert(0, id_)
    table.append(inputs)

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

    for item in table:
        if item[0] == id_[0]:
            table.remove(item)

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
    data_names = ['month', 'day', 'year', 'type (in/out)', 'amount']

    for item in table:
        if item[0] == id_[0]:
            index = table.index(item)
            inputs = ui.get_inputs(data_names, ('Change data of %s record:' % id_[0]))
            inputs.insert(0, id_[0])
            table[index] = inputs

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    profit_years = []
    year_max = 0
    biggest_profit = 0

    for item in table:
        if item[4] == 'in':
            profit_years.append(item)

    for item in profit_years:
        if int(item[5]) > biggest_profit:
            year_max = item[3]

    return year_max


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    
