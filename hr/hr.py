# data structure:
# id: string
# Unique and random generated (at least 2 special char()expect: ';'), 2 number,
# 2 lower and 2 upper case letter)
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
    '''
    Prints name of module name and numbered names of functions

    Returns:
        None
    '''
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
    Displays a table with records given in table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Name", "Brth date"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    data_names = ['Name', 'Year']
    inputs = data_names[:]

    while not inputs[1].isdigit():
        inputs = ui.get_inputs(data_names, "Enter person info")

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
        ui.print_error_message("There isn't person with such ID!")
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
    exists = False
    for item in table:
        if item[0] == id_[0]:
            exists = True
    if exists:
        for i in range(len(table)):
            if table[i][0] == id_[0]:

                data_names = ['Name', 'Year']
                inputs = data_names[:]

                while not inputs[1].isdigit():
                    inputs = ui.get_inputs(data_names, "Enter person info")

                inputs.insert(0, id_[0])
                table[i] = inputs
    else:
        ui.print_error_message("There isn't person with such ID!")
    return table


def get_oldest_person(table):
    """
    Picks people who were born the earliest

    Args:
        table: list in which we look for oldest people

    Returns:
        list with oldest people
    """

    so_rted_years = common.bubble_so_rt([item[2] for item in table])
    oldest_people = [item[1] for item in table if item[2] == so_rted_years[0]]

    return oldest_people


def get_persons_closest_to_average(table):
    """
    Counts average age and picks people whos birth year is
    closest to the average

    Args:
        table: list in which we look for people closest to the average age

    Returns:
        list with people closest to the average age
    """
    average_year = common.get_average_number([int(item[2]) for item in table])
    differences_list = [abs(int(item[2]) - average_year) for item in table]
    minimum_difference = common.get_min_number(differences_list)
    closest_people = []
    for i in range(len(differences_list)):
        if differences_list[i] == minimum_difference:
            closest_people.append(table[i][1])
    return closest_people
