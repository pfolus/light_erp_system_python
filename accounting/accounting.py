# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'),
# 2 number, 2 lower and 2 upper case letter)
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
    option = ""
    reading_file_successful = True
    try:
        table = data_manager.get_table_from_file('accounting/items.csv')
    except FileNotFoundError:
        ui.print_error_message('File not found, couldn\'t run the module.')
        reading_file_successful = False

    while option != "0" and reading_file_successful:
        handle_menu()
        try:
            table, option = choose(table)
        except KeyError as err:
            ui.print_error_message(err)
    if reading_file_successful:
        data_manager.write_table_to_file("accounting/items.csv", table)


def handle_menu():
    '''
    Prints name of module name and numbered names of functions

    Returns:
        None
    '''
    menu_name = 'Accounting Manager:'
    menu_options = ['Show records', 'Add a record',
                    'Remove a record', 'Update a record',
                    'Most profitable year', 'Average profit per item']

    ui.print_menu(menu_name, menu_options, 'Exit to menu')


def choose(table):
    '''
    Asks user to choose a number of special feature in this module
    Gets inputs needed to run chosen function
    User may exit this module by typing '0'


    Returns:
        table = list of lists
        option = string
    '''
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
        result = which_year_max(table)
        ui.print_result(result, "Most profitable year")
    elif option == "6":
        year = ui.get_inputs(['Year: '], 'Average profit per item in given year.')
        while not year[0].isdigit():
            year = ui.get_inputs(['Year: '], 'Average profit per item in given year.')
        avg_profit = avg_amount(table, int(year[0]))
        ui.print_result(str(avg_profit), 'Average profit per item:')

    return table, option


def show_table(table):
    """
    Displays a table with records given in table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    data_names = ['month', 'day', 'year', 'type (in/out)', 'amount']
    possible_types = ['in', 'out']
    inputs = data_names[:]

    while not inputs[0].isdigit() or not inputs[1].isdigit()\
            or not inputs[2].isdigit() or inputs[3] not in possible_types\
            or not inputs[4].isdigit():
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

    data_labels = ['Month: ', 'Day: ', 'Year: ', 'Type (in/out): ', 'Amount: ']
    possible_types = ['in', 'out']
    new_data = data_labels[:]

    while not new_data[0].isdigit() or not new_data[1].isdigit()\
            or not new_data[2].isdigit() or new_data[3] not in possible_types\
            or not new_data[4].isdigit():

        new_data = ui.get_inputs(data_labels, ('Change data of %s record:' % id_[0]))

    new_data.insert(0, id_[0])

    for i in range(len(table)):
        if table[i][0] == id_[0]:
            table[i] = new_data
    return table


def which_year_max(table):
    '''
    Function checks every record with profit (labeled as 'in')
    Returns the year with highest profit

    Returns:
        year_max = int
    '''
    profit_years = []
    year_max = 0
    biggest_profit = 0

    for item in table:
        if item[4] == 'in':
            profit_years.append(item)

    for item in profit_years:
        if int(item[5]) > biggest_profit:
            year_max = item[3]
    return int(year_max)


def avg_amount(table, year):
    '''
    Function checks records from the date provided by user
    Every in and out value is summed, and divided by /
    amount of logs from provided year, giving an average profit

    Args:
        table: list with records
        year: ueser's input turned to integer

    Returns:
        avg_profit = int
    '''
    profit = 0
    data_of_given_year = []

    for item in table:
        if int(item[3]) == year:
            data_of_given_year.append(item)

    for record in data_of_given_year:
        if record[4] == 'in':
            profit += int(record[5])
        elif record[4] == 'out':
            profit -= int(record[5])
    try:
        avg_profit = profit / len(data_of_given_year)
        return avg_profit
    except ZeroDivisionError:
        ui.print_error_message('There are no record from provided year')
