# This is a sample Python script.
# Doc https://docs.python.org/uk/3/library/tkinter.html
# Ex: https://realpython.com/python-gui-tkinter/
# Installation: pip3 install tk
import tkinter as tk
from loguru import logger
import calc_main as cm
import ast

# Global Constants Values
mywindow = tk.Tk()
BUTTON_SQUARE = 2
COLORS = ["gray", "black"]
TITLE = "Calculator"


# Static methods

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
        entry.delete(tk.END)


def clear(entry):
    """
    Method - Clear entry field
    :param entry: 
    :return: 
    """
    if entry:
        entry.delete(0, tk.END)


# dict_coordinat_for_button = {'+': [2,7],
#                              '-':[2,8]}

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
        # if dict_coordinat_for_button.get(button_text):
        #     btn_row, btn_column = dict_coordinat_for_button.get(button_text)
        #     pass

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
            command=lambda: sqrt_entry(btn_entry))
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
        return float(value)


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


def sqrt_entry(entry):
    """
    Method: SQRT method on button
    :param entry:
    :return:
    """
    # Step 1 - Get data from entry field. Data is always string!
    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")

    a = get_num(list_of_entries[0])
    ret_val = cm.sqrt(a)
    logger.debug(f"Result: {ret_val}")

    entry.delete(0, tk.END)
    entry.insert(100, ret_val)


def readenry(entry):
    """
    Algorithm!!!
    
    User enter value(Number) (Can be integer or float)
    User press operator button (+/-*...)
    User enter value(Number) (Can be integer or float)
    User enter '=' to get result
    
    :param entry: 
    :return: 
    """
    # Step 1 - Get data from entry field. Data is always string!
    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")

    # Step 2 - Get correct types of values a and b
    ret_val = None
    a, b = get_a_and_b(list_of_entries)

    # Step 3 - Perform calculation
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
    entry.insert(100, ret_val)
    logger.debug(f"Result: {ret_val}")



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

    create_calc_button(button_text=' + ', btn_entry=entry, btn_row=2, btn_column=7)
    create_calc_button(button_text=' - ', btn_entry=entry, btn_row=2, btn_column=8)
    create_calc_button(button_text=' * ', btn_entry=entry, btn_row=3, btn_column=7)
    create_calc_button(button_text=' / ', btn_entry=entry, btn_row=3, btn_column=8)
    create_calc_button(button_text=' ** ', btn_entry=entry, btn_row=4, btn_column=7)
    create_sqrt_button(button_text=' R ', btn_entry=entry, btn_row=4, btn_column=8)
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