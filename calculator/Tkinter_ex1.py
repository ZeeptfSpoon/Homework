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
                                 '**': [4, 7]}

dict_coordinat_for_button = {'8': [2, 5],
                             '5': [3, 5],
                             '2': [4, 5],
                             '9': [2, 6],
                             '6': [3, 6],
                             '3': [4, 6],
                             '7': [2, 4],
                             '4': [3, 4],
                             '1': [4, 4],
                             '0': [5, 5],
                             '.': [5, 6]}
##############################################################################################################


MUL = '*'
DIV = '/'
PLS = '+'
MIS = '-'
SQR = 'R'
POW = '**'


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
    :param btn_entry
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
def create_calc_button(button_text, btn_entry):
    """
    Method: Create and place button on Calculator
    :param btn_entry
    :param button_text
    :param btn_row
    :param btn_column
    :return: button
    """
    button = None

    if button_text is not None and btn_entry is not None:
        if dict_coordinat_for_button.get(button_text.strip(" ")):
            btn_row, btn_column = dict_coordinat_for_button.get(button_text.strip(" "))

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
    :param btn_entry
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
    :param btn_entry
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
    :param btn_entry
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
    :param btn_entry
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


########################################################################################################################

def del_of_used(functions: str, data: list):
    """
    Method
    :param data:
    :param functions:
    :param list_of_entries:
    :return:
    """
    if data is not None:
        del data[(data.index(functions) - 1):(data.index(functions) + 2)]
    else:
        logger.error("data is None")


def get_variables_for_calculation(entries, idx):
    """
    Method for finding a and b in easy calc
    :param entries: list_of_entries
    :param idx: index of operator
    :return:
    """
    if isinstance(entries, list):
        if idx is not None:
            if len(entries) >= idx + 1:
                a = float(entries[idx - 1])
                b = float(entries[idx + 1])
    return a, b


def calculate_data(what: str, data: list, indx: int, value: float):
    """
    Method executes calculations
    :param what:
    :param data:
    :param indx: index of operator
    :param value:
    :return:
    """
    del_of_used(what, data)
    data.insert(indx - 1, value)


def calculate_3_last(data: list):
    """

    :param data:
    :return:
    """
    ret_val = None
    a, b = get_a_and_b(data)
    if '+' in data:
        ret_val = cm.summ(a, b)
    elif '-' in data:
        ret_val = cm.margin(a, b)
    elif '*' in data:
        ret_val = cm.multiply(a, b)
    elif '/' in data:
        ret_val = cm.divide(a, b)
    elif '**' in data:
        ret_val = cm.power(a, b)
    return ret_val


def calc_fnct(data: list, symbol: str, fnct: any):
    """
    method: takeout a and b do calculations, return answer in place of a and b
    :param fnct: operator from calc_main library: cm.example
    :param data: list_of_entries
    :param symbol: symbol of operator for ex SUM or +
    :return:
    """
    idx = data.index(symbol)
    a, b = get_variables_for_calculation(data, idx)
    ret_val = fnct(a, b)
    calculate_data(symbol, data, idx, ret_val)


def sqrt_in_law(data: list, fnct: str):
    """
    method for Square root operator with changing of Data
    :param data: list_of_entries
    :param fnct: SQR
    :return:
    """
    idx = data.index(fnct)
    a = float(data[idx - 1])
    logger.debug(a)
    ret_val = cm.sqrt(a)
    del data[(idx - 1):(idx + 2)]
    data.insert(idx - 1, ret_val)


def first_to_go_meth(f1: str, f2: str, data: list, cmf2: any):
    """
    method represents easy algorythm to find which operator has to be executed first.
    :param f1: operator 1 ex.: DIV
    :param f2: operator 2 ex.: MUL
    :param data: list of sequences which human inserted (list_of_entries)
    :param cmf2: method from calc_main library #always starts from: cm.example
    :return: changed data or None
    """
    if f1 in data:
        priority_mult = data.index(f1)
    if f2 in data:
        priority_dev = data.index(f2)

    first_to_go = priority_mult if priority_mult < priority_dev else priority_dev
    METHOD = f1 if priority_mult < priority_dev else f2

    a, b = get_variables_for_calculation(data, first_to_go)
    ret_val = cmf2(a, b)
    calculate_data(METHOD, data, first_to_go, ret_val)


def first_to_go_meth_sqrandpow(f1: str, f2: str, data: list, cmf2: any):
    """
    method represents easy algorythm to find which operator has to be executed first if there is SQRT or POW
    :param f1: operator 1 ex.: SQRT
    :param f2: operator 2 ex.: POW
    :param data: list of sequences which human inserted (list_of_entries)
    :param cmf2: method from calc_main library #always starts from: cm.example
    :return: changed data or None
    """
    if f1 in data:
        priority_mult = data.index(f1)
    if f2 in data:
        priority_dev = data.index(f2)

    first_to_go = priority_mult if priority_mult < priority_dev else priority_dev
    METHOD = f1 if priority_mult < priority_dev else f2

    if METHOD == f2:
        a, b = get_variables_for_calculation(data, first_to_go)
        ret_val = cmf2(a, b)
        calculate_data(METHOD, data, first_to_go, ret_val)
    if METHOD == f1:
        a = float(data[first_to_go - 1])
        ret_val = cm.sqrt(a)
        calculate_data(METHOD, data, first_to_go, ret_val)


def readenry(entry):  # _with_sequences
    """
    Algorithm!!!

    User enter value(Number) (Can be integer or float)
    User press operator button (+/-*...)
    User enter value(Number) (Can be integer or float)
    User repeat upper stages until full fnx will be on the entrance field
    program reads the line and in depend on function decides what to exe first

    :param entry:
    :return:
    """
    # Step 1 - Get data from entry field. Data is always string!
    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries: list = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")
    functions = None

    # Step 2 execute order 66

    raw_data = entry.get()
    logger.debug(f"Raw: {raw_data}")

    list_of_entries: list = raw_data.split(" ")
    logger.debug(f"Split: {list_of_entries}")
    functions = None

    ###################################################################################################################
    # Example: 16 R  / 4 ** 3 + 2 = 3
    list_of_entries = ['16', 'R', ' ', '/', '4', '**', '3', '+', '2']

    # SET NAMING VARIABLES

    # Prepare Environment for testing

    if SQR in list_of_entries and POW in list_of_entries:
        first_to_go_meth_sqrandpow(SQR, POW, list_of_entries, cm.power)

    while SQR in list_of_entries:
        sqrt_in_law(list_of_entries, SQR)

    while POW in list_of_entries:
        calc_fnct(list_of_entries, POW, cm.power)

    while len(list_of_entries) > 3:
        priority_mult = 0
        priority_dev = 0
        METHOD = None

        if MUL in list_of_entries and DIV in list_of_entries:
            first_to_go_meth(MUL, DIV, list_of_entries, cm.divide)
            continue
        ############################################################################################################
        if MUL in list_of_entries:
            calc_fnct(list_of_entries, MUL, cm.multiply)
        if DIV in list_of_entries:
            calc_fnct(list_of_entries, DIV, cm.divide)
        if PLS in list_of_entries:
            calc_fnct(list_of_entries, PLS, cm.summ)
        if MIS in list_of_entries:
            calc_fnct(list_of_entries, MIS, cm.margin)
    ###################################################################################################################

    ret_val = calculate_3_last(list_of_entries)
    pass
    ret_val = list_of_entries
    entry.delete(0, tk.END)
    if ret_val is None:
        notify("oppsie", command=lambda: print('clicked'))
    else:
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
    # TODO
    readenry(entry)  # Testing Algorithm. RAT.
    ##############################################################################################################

    create_func_button(button_text=' + ', btn_entry=entry)
    create_func_button(button_text=' - ', btn_entry=entry)
    create_func_button(button_text=' * ', btn_entry=entry)
    create_func_button(button_text=' / ', btn_entry=entry)
    create_func_button(button_text=' ** ', btn_entry=entry)
    create_sqrt_button(button_text=' R ', btn_entry=entry, btn_row=4, btn_column=8)
    ##############################################################################################################
    create_calc_button(button_text='8', btn_entry=entry)
    create_calc_button(button_text='5', btn_entry=entry)
    create_calc_button(button_text='2', btn_entry=entry)
    create_calc_button(button_text='9', btn_entry=entry)
    create_calc_button(button_text='6', btn_entry=entry)
    create_calc_button(button_text='3', btn_entry=entry)
    create_calc_button(button_text='7', btn_entry=entry)
    create_calc_button(button_text='4', btn_entry=entry)
    create_calc_button(button_text='1', btn_entry=entry)
    create_calc_button(button_text='0', btn_entry=entry)

    create_calc_button(button_text='.', btn_entry=entry)
    ##############################################################################################################
    mywindow.mainloop()
