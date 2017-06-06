# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
        id_ = ui.get_inputs(["Enter person's id: "], "")
        table = remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter person's id: "], "")
        table = update(table, id_)
    elif option == "5":
        result = get_oldest_person(table)
        ui.print_result(result, "Oldest people")
    elif option == "6":
        result = get_persons_closest_to_average(table)
        ui.print_result(result, "People closest to the average age")
    return table, option


def handle_menu():
    options = ["Show table",
               "Add person",
               "Remove person",
               "Update person info",
               "Get oldest person",
               "Get person closest to average age"]

    ui.print_menu("Human resources manager", options, "Exit to menu")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("hr/persons.csv")
    option = ""
    while option != "0":
        handle_menu()
        table, option = choose(table)
    data_manager.write_table_to_file("hr/persons.csv", table)


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

    inputs = ui.get_inputs(["Name", "Year"], "Enter person info")
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

    for item in table:
        if item[0] == id_[0]:
            inputs = ui.get_inputs(["Name", "Year"], "Enter person info")
            inputs.insert(0, id_[0])
            table[table.index(item)] = inputs

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    sorted_years = common.bubble_sort([item[2] for item in table])
    oldest_people = [item[1] for item in table if item[2] == sorted_years[0]]

    return oldest_people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
