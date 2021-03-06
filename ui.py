def get_max_number(numbers):
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number


def print_list_elements(results):

    for i in range(len(results)):
        print("{:4}{}. {}".format('', str(i+1), results[i]))


def print_dict_elements(results):

    for key, value in results.items():
        print('{:4}{}: {}'.format('', key.capitalize(), value))


def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """
    # Appends dictionary with widest record's length
    column_widths = {}
    total_width = 0

    for i in range(len(title_list)):
        widths = []
        widths.append(len(str(title_list[i])))
        for item in table:
            widths.append(len(str(item[i])))
        max_column_width = get_max_number(widths) + 4
        column_widths["column_" + str(i)] = max_column_width
        total_width += max_column_width
    total_width += len(title_list) + 1

    # Printing
    print("/" + "-" * (total_width - 2) + "\\")
    print("|", end="")
    for i in range(len(title_list)):
        print("{:^{}}".format(title_list[i], column_widths["column_" + str(i)]), "|", end="", sep="")
    print()
    for i in range(len(table)):
        print("|", end="")
        for j in range(len(table[i])):
            print("{:-^{}}".format("", column_widths["column_" + str(j)]), "|", end="", sep="")
        print()
        print("|", end="")
        for j in range(len(table[i])):
            print("{:^{}}".format(table[i][j], column_widths["column_" + str(j)]), "|", end="", sep="")
        print()
    print("\\" + "-" * (total_width - 2) + "/")
    print()


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(label + ":")
    if type(result) == str or type(result) == int:
        print(result)
    elif type(result) == list:
        print_list_elements(result)
    elif type(result) == dict:
        print_dict_elements(result)
    print()


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(title + ":")
    counter = 1
    for option in list_options:
        print("{:>7}".format('(' + str(counter) + ')') + " {}".format(option))
        counter += 1
    print("{:>7}".format('(0)') + " {}".format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for item in list_labels:
        user_input = input(item + " ")
        inputs.append(user_input)
    print()

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print("Error: ", message)
    print()
