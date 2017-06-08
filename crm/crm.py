# data structure:
# id: string
# Unique and randomly generated (at least 2 special char()expect: ';'),
# 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
        id_ = ui.get_inputs(['ID: '], 'Provide ID of customer you want to remove: ')
        table = remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(['ID: '], 'Provide ID of customer you want to update: ')
        table = update(table, id_)
    elif option == "5":
        longest_name_id = get_longest_name_id(table)
        ui.print_result(longest_name_id, 'ID of a customer with a longest name')
    elif option == "6":
        subscription_list = get_subscribed_emails(table)
        ui.print_result(subscription_list, 'List of customers with a subscription')
    return table, option


def handle_menu():
    '''
    Prints name of module name and numbered names of functions

    Returns:
        None
    '''
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get longest name id",
               "Get subscribed emails(table)"]

    ui.print_menu("Customer Relationship Management", options, "Return to menu")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('crm/customers.csv')
    option = ""
    while option != "0":
        handle_menu()
        table, option = choose(table)
    data_manager.write_table_to_file("crm/customers.csv", table)


def show_table(table):
    """
    Displays a table with records given in table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Name", "E-mail", "Subscribed"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    generated = common.generate_random(table)

    list_labels = ['Name: ', 'Email: ',
                   'Is she/he subscribed to the newsletter? [1 = yes / 0 = no]']

    possible_types = ['0', '1']
    inputs = list_labels[:]

    while not inputs[2] in possible_types:
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

    exist = False
    for item in table:
        if item[0] == id_[0]:
            exist = True

    if exist:

        list_labels = ['Name: ', 'Email: ',
                       'Is she/he subscribed to the newsletter? [1 = yes / 0=no]']
        possible_types = ['0', '1']
        new_data = list_labels[:]

        while not new_data[2] in possible_types:
            new_data = ui.get_inputs(list_labels, 'Enter customers new data: ')
        new_data.insert(0, id_[0])

        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table[i] = new_data
    else:
        ui.print_error_message("There isn't person with such ID!")

    return table


def get_longest_name_id(table):
    """
    Picks id of customer with longest name

    Args:
        table: list in which we look for customers

    Returns:
        string: id of person with longes name
    """
    longest_name = ''
    for item in table:
        if len(item[1]) > len(longest_name):
            longest_name = item[1]
            longest_name_id = item[0]
        elif len(item[1]) == len(longest_name):
            if item[1] < longest_name:
                longest_name = item[1]
                longest_name_id = item[0]
    return longest_name_id


def get_subscribed_emails(table):
    '''
    Picks e-mails which subscribed

    Args:
        table: list in which we look for emails

    Returns:
        list with subscribed e-mails
    '''
    subscription_list = []
    for item in table:
        if item[3] == '1':
            single_subscription = item[2] + ';' + item[1]
            subscription_list.append(single_subscription)

    return subscription_list
