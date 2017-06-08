# data structure:
# id: string
# Unique and random generated (at least 2 special char()expect: ';'),
# 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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
        table = data_manager.get_table_from_file('sales/sales.csv')
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
        data_manager.write_table_to_file('sales/sales.csv', table)


def handle_menu():
    '''
    Prints name of module name and numbered names of functions

    Returns:
        None
    '''
    menu_name = 'Sales Manager'
    menu_options = ['Show records', 'Add a record',
                    'Remove a record', 'Update a record',
                    'Lowest price game', 'Items sold between dates']

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
        low_price_id = get_lowest_price_item_id(table)
        ui.print_result(low_price_id, 'ID of item sold for the lowest price')
    elif option == "6":
        inputs = ['Month from: ', 'Day from: ', 'Year from: ',
                  'Month to: ', 'Day to: ', 'Year to: ']
        dates = inputs[:]
        while not dates[0].isdigit() or not dates[1].isdigit()\
            or not dates[2].isdigit() or not dates[3].isdigit()\
                or not dates[4].isdigit() or not dates[5].isdigit():

            dates = ui.get_inputs(inputs, 'Items sold between dates')

        sold_items = get_items_sold_between(table, dates[0], dates[1], dates[2], dates[3], dates[4], dates[5])
        ui.print_result(sold_items, 'Items sold between dates')
    return table, option


def show_table(table):
    """
    Displays a table with records given in table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Title", "Price",
                  "Month", "Day", "Year"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    data_names = ['Title', 'Price', 'Month', 'Day', 'Year']

    inputs = data_names[:]

    while not inputs[1].isdigit() or not inputs[2].isdigit()\
            or not inputs[3].isdigit() or not inputs[4].isdigit():
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

    data_labels = ['Title', 'Price', 'Month', 'Day', 'Year']

    new_data = data_labels[:]

    while not new_data[1].isdigit() or not new_data[2].isdigit()\
            or not new_data[3].isdigit() or not new_data[4].isdigit():
        new_data = ui.get_inputs(data_labels, ('Change data of %s record:' % id_[0]))

    new_data.insert(0, id_[0])

    for i in range(len(table)):
        if table[i][0] == id_[0]:
            table[i] = new_data
    return table


def get_lowest_price_item_id(table):
    '''
    Function check the records to find the item sold for the lowest price
    If there are more than one item with the lowest price/
    function returns the first by descending alphabetical order

    Returns:
        lowest_price_item_id = string
    '''
    game_names_with_id = {}
    so_rted_game_names = []
    lowest_price = table[0][2]
    for item in table:
        if int(item[2]) < int(lowest_price):
            lowest_price = item[2]

    lowest_price_item_id = []
    for item in table:
        if item[2] == lowest_price:
            lowest_price_item_id.append(item[0])
            game_names_with_id[item[0]] = item[1]

    if len(lowest_price_item_id) > 1:
        so_rted_game_names = common.get_max_number(list(game_names_with_id.values()))
        for key, value in game_names_with_id.items():
            if value == so_rted_game_names:
                return key
    else:
        return lowest_price_item_id[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    '''
    Function checks game records sold between provided dates
    (from_date < sale_date < to_date)

    Args:
        table = list of lists
        month_from, day_from, year_from = string
        month_to, day_to, year_to = string

    Return:
        sold_items = list of lists
    '''
    sold_items = []
    temp_table = [x[:] for x in table]

    for item in temp_table:
        game_year = int(item[5])
        game_month = int(item[3])
        game_day = int(item[4])
        year_from, month_from, day_from = int(year_from), int(month_from), int(day_from)
        year_to, month_to, day_to = int(year_to), int(month_to), int(day_to)

        if game_year >= year_from and game_year <= year_to:
            if game_year != year_from and game_year != year_to:  # game year between provided years
                sold_items.append(item)
            elif game_year == year_from:  # game year the same as year from
                if game_month > month_from:
                    if year_from == year_to:
                        if game_month < month_to:
                            sold_items.append(item)
                    elif year_from != year_to:
                        sold_items.append(item)
                elif game_month == month_from:
                    if game_day > day_from:
                        sold_items.append(item)
            elif game_year == year_to:  # game year the same as year to
                if game_month < month_to:
                    sold_items.append(item)
                elif game_month == month_to:
                    if game_day < day_to:
                        sold_items.append(item)

    for x in range(2, 6):
        for i in sold_items:
            i[x] = int(i[x])

    return sold_items
