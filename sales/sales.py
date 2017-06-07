# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
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

    table = data_manager.get_table_from_file('sales/sales.csv')

    option = ""
    while option != "0":
        handle_menu()
        try:
            table, option = choose(table)
        except KeyError as err:
            ui.print_error_message(err)
    data_manager.write_table_to_file('sales/sales.csv', table)


def handle_menu():

    menu_name = 'Sales Manager:'
    menu_options = ['Show records', 'Add a record',
                    'Remove a record', 'Update a record',
                    'Lowest price game', 'Items sold between dates']

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
        low_price_id = get_lowest_price_item_id(table)
        ui.print_result(low_price_id, 'ID of item sold for the lowest price')
    elif option == "6":
        inputs = ['Month from: ', 'Day from: ', 'Year from: ',
                  'Month to: ', 'Day to: ', 'Year to: ']
        dates = ui.get_inputs(inputs, 'Items sold between dates:')
        sold_items = get_items_sold_between(table, dates[0], dates[1], dates[2], dates[3], dates[4], dates[5])
        ui.print_result(sold_items, 'Items sold between dates:')
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

    data_names = ['Title', 'Price', 'Month', 'Day', 'Year']

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

    data_labels = ['Title: ', 'Price: ', 'Month: ', 'Day: ', 'Year: ']
    new_data = ui.get_inputs(data_labels, ('Change data of %s record:' % id_[0]))
    new_data.insert(0, id_[0])

    for i in range(len(table)):
        if table[i][0] == id_[0]:
            table[i] = new_data
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):

    lowest_price = table[0][2]
    for item in table:
        if item[2] < lowest_price:
            lowest_price = item[2]

    lowest_price_item_id = []
    for item in table:
        if item[2] == lowest_price:
            lowest_price_item_id.append(item[0])

    if len(lowest_price_item_id) > 1:
        lowest_price_item_id = common.get_max_number(lowest_price_item_id)
        return lowest_price_item_id[0]
    else:
        return lowest_price_item_id[0]



# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    sold_items = []

    date_from = ((int(year_from) - 1) * 365) + (int(month_from) * 30 + int(day_from))
    date_to = ((int(year_to) - 1) * 365) + (int(month_to) * 30 + int(day_to))

    for item in table:
        date = ((int(item[5]) - 1) * 365) + ((int(item[3]) * 30) + int(item[4]))
        
        if date >= date_from and date <= date_to:
            sold_items.append(item)

    return sold_items
