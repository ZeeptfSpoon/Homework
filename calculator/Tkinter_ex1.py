# This is a sample Python script.
# Doc https://docs.python.org/uk/3/library/tkinter.html
# Ex: https://realpython.com/python-gui-tkinter/
# Installation: pip3 install tk
import tkinter as tk

from loguru import logger

import calc_main as cm

# Global Constants Values
mywindow = tk.Tk()
BUTTON_SQUARE = 2
COLORS = ["gray", "black"]
TITLE = "BRUTAL Calculator"

dict_coordinat_for_fnctbutton = {'+': [2, 7],
                                 '-': [2, 8],
                                 '*': [3, 7],
                                 '/': [3, 8],
                                 '**': [4, 7]

                                 }


# Static methods

def notify(message="Hello World!", image=None, timeout=5000, command=None):
    def on_click(event=None):  # wrapper
        if command: command()
        popup.destroy()

    popup = tk.Toplevel(bg='black', relief=tk.RAISED, bd=3)
    popup.overrideredirect(True)
    popup.geometry("200x50-300-300")
    lbl = tk.Message(popup, bg='black', fg='white', border=2, text=message)
    lbl.pack()
    lbl.bind('<1>', on_click)
    if timeout: popup.after(timeout, popup.destroy)


def button_enter_val(entry, val):
    """
    Method insert text label on top of the button
    :param entry: 
    :param val: 
    :return: 
    """
    logger.debug(f"Button {val}")
    if entry:
        entry.insert(100, val)


def backspace(entry):
    """
    Method: function for button which will be deleating last number
    :param entry: 
    :return: 
    """
    if entry:
        entry.delete(len(entry.get()) - 1, tk.END)


def clear(entry):
    """
    Method - Clear entry field
    :param entry: 
    :return: 
    """
    if entry:
        entry.delete(0, tk.END)


##############################################################################################################
def create_func_button(button_text, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :return: button
    """
    button = None

    if button_text is not None and btn_entry is not None:
        if dict_coordinat_for_fnctbutton.get(button_text.strip(" ")):
            btn_row, btn_column = dict_coordinat_for_fnctbutton.get(button_text.strip(" "))

            if btn_row is not None and btn_column is not None:
                button = tk.Button(
                    text=button_text,
                    width=BUTTON_SQUARE, height=BUTTON_SQUARE,
                    bg=COLORS[0], fg=COLORS[1],
                    command=lambda: button_enter_val(btn_entry, val=button_text))
                button.grid(row=btn_row, column=btn_column)
    return button


##############################################################################################################
# create_calc_button(button_text='8', btn_entry=entry, btn_row=2, btn_column=5)
# create_calc_button(button_text='5', btn_entry=entry, btn_row=3, btn_column=5)
# create_calc_button(button_text='2', btn_entry=entry, btn_row=4, btn_column=5)
# create_calc_button(button_text='9', btn_entry=entry, btn_row=2, btn_column=6)
# create_calc_button(button_text='6', btn_entry=entry, btn_row=3, btn_column=6)
# create_calc_button(button_text='3', btn_entry=entry, btn_row=4, btn_column=6)
# create_calc_button(button_text='7', btn_entry=entry, btn_row=2, btn_column=4)
# create_calc_button(button_text='4', btn_entry=entry, btn_row=3, btn_column=4)
# create_calc_button(button_text='1', btn_entry=entry, btn_row=4, btn_column=4)
# create_calc_button(button_text='0', btn_entry=entry, btn_row=5, btn_column=5)
#
# create_calc_button(button_text='.', btn_entry=entry, btn_row=5, btn_column=6)


def create_calc_button(button_text, btn_row, btn_column, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None

    if button_text is not None and btn_row is not None and btn_column is not None and btn_entry is not None:
        # if dict_coordinat_for_fnctbutton.get(button_text):
        #     btn_row, btn_column = dict_coordinat_for_fnctbutton.get(button_text)
        # pass

        button = tk.Button(
            text=button_text,
            width=BUTTON_SQUARE, height=BUTTON_SQUARE,
            bg=COLORS[0], fg=COLORS[1],
            command=lambda: button_enter_val(btn_entry, val=button_text))
        button.grid(row=btn_row, column=btn_column)
    return button


def create_bcksp_button(button_text, btn_row, btn_column, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None
    if button_text is not None and btn_row is not None and btn_column is not None and btn_entry is not None:
        button = tk.Button(
            text=button_text,
            width=BUTTON_SQUARE + 4, height=BUTTON_SQUARE,
            bg=COLORS[0], fg=COLORS[1],
            command=lambda: backspace(btn_entry))
        button.grid(row=btn_row, column=btn_column)
    return button


def create_sqrt_button(button_text, btn_row, btn_column, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None
    if button_text is not None and btn_row is not None and btn_column is not None and btn_entry is not None:
        button = tk.Button(
            text=button_text,
            width=BUTTON_SQUARE, height=BUTTON_SQUARE,
            bg=COLORS[0], fg=COLORS[1],
            command=lambda: button_enter_val(btn_entry, val=button_text))
        button.grid(row=btn_row, column=btn_column)
    return button


def create_equal_button(button_text, btn_row, btn_column, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None
    if button_text is not None and btn_row is not None and btn_column is not None and btn_entry is not None:
        button = tk.Button(
            text=button_text,
            width=BUTTON_SQUARE, height=BUTTON_SQUARE,
            bg=COLORS[0], fg=COLORS[1],
            command=lambda: readenry(btn_entry))
        button.grid(row=btn_row, column=btn_column)
    return button


def create_clear_button(button_text, btn_row, btn_column, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry:
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None
    if button_text is not None and btn_row is not None and btn_column is not None and btn_entry is not None:
        button = tk.Button(
            text=button_text,
            width=BUTTON_SQUARE + 4, height=BUTTON_SQUARE,
            bg=COLORS[0], fg=COLORS[1],
            command=lambda: clear(btn_entry))
        button.grid(row=btn_row, column=btn_column)
    return button


########################################################################################################################


def get_num(value):
    """
    Get int, float form string
    :param value:
    :return:
    # TODO: ret_val = ast.literal_eval(value)
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return None


def get_a_and_b(list_of_entries):
    """
    Method:
    :param list_of_entries:
    :return:
    """
    val_a = None
    val_b = None
    if list_of_entries and len(list_of_entries) > 2:
        val_a = get_num(list_of_entries[0])
        val_b = get_num(list_of_entries[2])
    else:
        logger.error("List from entry is empty")
    return val_a, val_b


# def sqrt_entry(entry):
#     """
#     Method: SQRT method on button
#     :param entry:
#     :return:
#     """
#     # Step 1 - Get data from entry field. Data is always string!
#     raw_data = entry.get()
#     logger.debug(f"Raw: {raw_data}")
#
#     list_of_entries = raw_data.split(" ")
#     logger.debug(f"Split: {list_of_entries}")
#
#     a = get_num(list_of_entries[0])
#     entry.delete(0, tk.END)
#     if a is not None:
#         ret_val = cm.sqrt(a)
#         logger.debug(f"Result: {ret_val}")
#         entry.insert(100, ret_val)
#     else:
#         notify("PRINT NORMAL VALUE MF", command=lambda: print('clicked'))


def readenry(entry):         #_with_sequences
    """
    Algorithm!!!

    User enter value(Number) (Can be integer or float)
    User press operator button (+/-*...)
    User enter value(Number) (Can be integer or float)
    User repeat upper stages until full fnx will be on the entrance field
    program reads the line and in depend of function decides what to exe first

    :param entry:
    :return:
    """
    # Step 1 - Get data from entry field. Data is always string!
    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries: object = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")
    functions = None
    # Step 2 execute order 66
    # while "R" in list_of_entries:  # we need to think about it
    #     a = float(list_of_entries[(list_of_entries.index("R") - 1)])
    #     ret_val = cm.square(a)
    #     idx = list_of_entries.index("R")
    #     del_of_used("R")
    #     list_of_entries.insert(idx - 1, ret_val)
    #     while len(list_of_entries) >= 3:

    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries: object = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")
    functions = None

    def del_of_used(functions):
        del list_of_entries[(list_of_entries.index(functions) - 1):(list_of_entries.index(functions) + 2)]

    # Step 2 execute order 66
    while len(list_of_entries) >= 3:
        if "*" in list_of_entries or "/" in list_of_entries:  # here we need to get position of "*" in list of entries
            # logger.debug(list_of_entries.index("*" or "/"))
            # a = float(list_of_entries[(list_of_entries.index("*" or "/") - 1)])
            # b = float(list_of_entries[(list_of_entries.index("*" or "/") + 1)])
            # logger.debug(a)
            # logger.debug(b)
            if "*" in list_of_entries:
                logger.debug(list_of_entries.index("*"))
                a = float(list_of_entries[(list_of_entries.index("*") - 1)])
                b = float(list_of_entries[(list_of_entries.index("*") + 1)])
                ret_val = cm.multiply(a, b)
                idx = list_of_entries.index("*")
                del_of_used("*")
                list_of_entries.insert(idx - 1,ret_val)  # 1 time it goes but 2nd time ret_val dnt wanna work -- complete
            elif "/" in list_of_entries:
                logger.debug(list_of_entries.index("/"))
                a = float(list_of_entries[(list_of_entries.index("/") - 1)])
                b = float(list_of_entries[(list_of_entries.index("/") + 1)])
                ret_val = cm.divide(a, b)
                idx = list_of_entries.index("/")
                del_of_used("/")
                list_of_entries.insert(idx - 1, ret_val)
        else:
            a, b = get_a_and_b(list_of_entries)
            if '+' in list_of_entries:
                idx = list_of_entries.index("+")
                ret_val = cm.summ(a, b)
                del_of_used("+")
                list_of_entries.insert(idx - 1, ret_val)
            elif '-' in list_of_entries:
                idx = list_of_entries.index("-")
                ret_val = cm.margin(a, b)
                del_of_used("-")
                list_of_entries.insert(idx - 1, ret_val)

    if a is not None and b is not None:
        a, b = get_a_and_b(list_of_entries)
        if '+' in list_of_entries:
            ret_val = cm.summ(a, b)
        elif '-' in list_of_entries:
            ret_val = cm.margin(a, b)
        elif '*' in list_of_entries:
            ret_val = cm.multiply(a, b)
        elif '/' in list_of_entries:
            ret_val = cm.divide(a, b)
        elif '**' in list_of_entries:
            ret_val = cm.power(a, b)

    entry.delete(0, tk.END)
    if ret_val is None:
        notify("oppsie", command=lambda: print('clicked'))
    else:
        entry.insert(100, ret_val)
        logger.debug(f"Result: {ret_val}")


# def readenry(entry):
#     """
#     Algorithm!!!
#
#     User enter value(Number) (Can be integer or float)
#     User press operator button (+/-*...)
#     User enter value(Number) (Can be integer or float)
#     User enter '=' to get result
#
#     :param entry:
#     :return:
#     """
#     # Step 1 - Get data from entry field. Data is always string!
#     raw_data = entry.get()
#     logger.debug(f"Raw: {raw_data}")
#
#     list_of_entries = raw_data.split(" ")
#     logger.debug(f"Split: {list_of_entries}")
#
#     # Step 2 - Get correct types of values a and b
#     ret_val = None
#     a, b = get_a_and_b(list_of_entries)
#
#     # Step 3 - Perform calculation
#     if a is not None and b is not None:
#         if '+' in list_of_entries:
#             ret_val = cm.summ(a, b)
#         elif '-' in list_of_entries:
#             ret_val = cm.margin(a, b)
#         elif '*' in list_of_entries:
#             ret_val = cm.multiply(a, b)
#         elif '/' in list_of_entries:
#             ret_val = cm.divide(a, b)
#         elif '**' in list_of_entries:
#             ret_val = cm.power(a, b)
#
#     entry.delete(0, tk.END)
#     if ret_val is None:
#         notify("hi I'm a popup", command=lambda: print('clicked'))
#     else:
#         entry.insert(100, ret_val)
#         logger.debug(f"Result: {ret_val}")


########################################################################################################################


if __name__ == '__main__':
    label = tk.Label(
        text="Calculator",
        foreground="cyan",  # Set the text color to white
        background="black",  # Set the background color to black
        width=10, height=3)
    label.grid(row=0, column=1)

    # Textbox
    entry = tk.Entry(mywindow, text=TITLE)
    # action_with_arg=buttonPress(entry=entry)
    textbutton = tk.Button(mywindow, text="Text Box")
    entry.grid(row=1, column=1)

    # Button
    create_clear_button(button_text='Clear', btn_entry=entry, btn_row=2, btn_column=1)
    create_bcksp_button(button_text="<----", btn_entry=entry, btn_row=3, btn_column=1)
    create_equal_button(button_text="=", btn_entry=entry, btn_row=5, btn_column=7)

    ##############################################################################################################

    create_func_button(button_text=' + ', btn_entry=entry)
    create_func_button(button_text=' - ', btn_entry=entry)
    create_func_button(button_text=' * ', btn_entry=entry)
    create_func_button(button_text=' / ', btn_entry=entry)
    create_func_button(button_text=' ** ', btn_entry=entry)
    create_sqrt_button(button_text=' R', btn_entry=entry, btn_row=4, btn_column=8)
    ##############################################################################################################
    create_calc_button(button_text='8', btn_entry=entry, btn_row=2, btn_column=5)
    create_calc_button(button_text='5', btn_entry=entry, btn_row=3, btn_column=5)
    create_calc_button(button_text='2', btn_entry=entry, btn_row=4, btn_column=5)
    create_calc_button(button_text='9', btn_entry=entry, btn_row=2, btn_column=6)
    create_calc_button(button_text='6', btn_entry=entry, btn_row=3, btn_column=6)
    create_calc_button(button_text='3', btn_entry=entry, btn_row=4, btn_column=6)
    create_calc_button(button_text='7', btn_entry=entry, btn_row=2, btn_column=4)
    create_calc_button(button_text='4', btn_entry=entry, btn_row=3, btn_column=4)
    create_calc_button(button_text='1', btn_entry=entry, btn_row=4, btn_column=4)
    create_calc_button(button_text='0', btn_entry=entry, btn_row=5, btn_column=5)

    create_calc_button(button_text='.', btn_entry=entry, btn_row=5, btn_column=6)
    ##############################################################################################################
    mywindow.mainloop()
