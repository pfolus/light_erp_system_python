# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
        id_ = ui.get_inputs(["Enter console's id: "], "")
        table = remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter console's id: "], "")
        table = update(table, id_)
    elif option == "5":
        result = get_available_items(table)
        ui.print_result(result, "Available consoles")
    elif option == "6":
        result = get_average_durability_by_manufacturers(table)
        ui.print_result(result, "Average durability by mafucaturer")
    return table, option


def handle_menu():
    options = ["Show table",
               "Add console",
               "Remove console",
               "Update console info",
               "Get available consoles",
               "Get average durability of consoles"]

    ui.print_menu("Inventory manager", options, "Exit to menu")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("inventory/inventory.csv")
    option = ""
    while option != "0":
        handle_menu()
        table, option = choose(table)
    data_manager.write_table_to_file("inventory/inventory.csv", table)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Name", "Manufacturer",
                  "Purchase date", "Durability"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    list_labels = ["Name", "Manufacturer",
                   "Purchase date", "Drurability"]

    inputs = list_labels[:]

    while not inputs[2].isdigit() or not inputs[3].isdigit():
        inputs = ui.get_inputs(list_labels, "Enter console info")
        
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
    removed = False
    for item in table:
        if item[0] == id_[0]:
            table.remove(item)
            removed = True
    if not removed:
        ui.print_error_message("There isn't console with such ID!")
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
    list_labels = ["Name", "Manufacturer",
                   "Purchase date", "Drurability"]
    exists = False
    for item in table:
        if item[0] == id_[0]:
            exists = True
    if exists:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                inputs = ui.get_inputs(list_labels, "Enter console info")
                inputs.insert(0, id_[0])
                table[i] = inputs
    else:
        ui.print_error_message("There isn't console with such ID!")
    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    available_items_list = []
    differences_list = [2017 - int(item[3]) for item in table]
    for i in range(len(differences_list)):
        if int(table[i][4]) >= differences_list[i]:
            row = [table[i][0], table[i][1],
                   table[i][2], int(table[i][3]),
                   int(table[i][4])]
            available_items_list.append(row)
    return available_items_list


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    durability_by_manufacturers = {}
    manufacturers_list = [item[2] for item in table]
    exclusive_manufacturers = list(set(manufacturers_list))
    for i in range(len(exclusive_manufacturers)):
        occurance = 0
        durability_sum = 0
        for j in range(len(manufacturers_list)):
            if exclusive_manufacturers[i] == manufacturers_list[j]:
                occurance += 1
                durability_sum += int(table[j][4])
        durability_by_manufacturers[exclusive_manufacturers[i]] = durability_sum / occurance
    return durability_by_manufacturers
