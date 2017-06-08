# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose(table):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
    elif option == "3":
        id_ = ui.get_inputs(['ID: '], 'Provide ID of a game you want to remove: ')
        table = remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(['ID: '], 'Provide ID of a game you want to update: ')
        table = update(table, id_)
    elif option == "5":
        result = get_counts_by_manufacturers(table)
        ui.print_result(result, 'Number of different games by each manufacturer')
    elif option == "6":
        manufacturers = [item[2] for item in table]
        manufacturer = ui.get_inputs(['Manufacturer: '], 'Provide a manufacturer of a game: ')
        if manufacturer[0] in manufacturers:
            result = get_average_by_manufacturer(table, manufacturer[0])
            ui.print_result(str(result), 'Average games of provided manufacturer in stock')
        else:
            ui.print_error_message("There isn't such manufacturer")
    return table, option


def handle_menu():
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get counts by manufacturers",
               "Get average by manufacturer",]

    ui.print_menu("Store Module", options, "Return to menu")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('store/games.csv')
    option = ""
    while option != "0":
        handle_menu()
        table, option = choose(table)
    data_manager.write_table_to_file("store/games.csv", table)


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

    generated = common.generate_random(table)

    list_labels = ['Title: ', 'Manufacturer: ', 'Price: ', 'Number in stock: ']

    inputs = list_labels[:]

    while not inputs[2].isdigit() or not inputs[3].isdigit():
        inputs = ui.get_inputs(list_labels, 'Provide data: ')
        
    inputs.insert(0, generated)
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

    removed = False

    for item in table:
        if item[0] == id_[0]:
            table.remove(item)
            removed = True

    if not removed:
        ui.print_error_message("There isn't a game with such ID!")
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

    exist = False
    for item in table:
        if item[0] == id_[0]:
            exist = True

    if exist:
        list_labels = ['Title: ', 'Manufacturer: ', 'Price: ', 'Number in stock: ']
        new_data = ui.get_inputs(list_labels, 'Enter customers new data: ')
        new_data.insert(0, id_[0])

        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table[i] = new_data
    else:
        ui.print_error_message("There isn't a game with such ID!")

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    #getting a list of manufacturers
    manufacturers = []
    for item in table:
        if item[2] not in manufacturers:
            manufacturers.append(item[2])

    manufacturers_games = {}

    for record in manufacturers:
        games_counter = 0
        for item in table:
            if item[2] == record:
                games_counter += 1
            manufacturers_games[record] = games_counter

    return manufacturers_games


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    games_counter = 0
    games_types = 0
    for item in table:
        if item[2] == manufacturer:
            games_counter += int(item[4])
            games_types += 1

    average_amount = games_counter / games_types

    return average_amount
