# This is a sample Python script.
# Doc https://docs.python.org/uk/3/library/tkinter.html
# Ex: https://realpython.com/python-gui-tkinter/
# Installation: pip3 install tk

import tkinter as tk
from typing import Tuple

mywindow = tk.Tk()


def tod(a, b):
    return print(a + b)


def clear(entry):
    entry.delete(0, tk.END)


def buttonSum():
    print("Button +")


def backspace(entry):  # function for button which will be deleating last number
    entry.delete(tk.END)


# def buttonEnterVal(entry, val):
#     print(f"Button {val}")
#     entry.insert(0, val)

def buttonEnterVal(entry, val):
    print(f"Button {val}")
    entry.insert(100, val)


def butn_print_number(event):
    print(event)


def readenry(entry):
    readed = entry.get()
    print(readed)
    for funkt in readed:
        if funct := "+":
            list = readed.split("+")
            print(list)
            a=int(list[0])
            b=int(list[1])
            x=a+b
        print(x)




if __name__ == '__main__':
    label = tk.Label(
        text="Calculator",
        foreground="cyan",  # Set the text color to white
        background="black",  # Set the background color to black
        width=10,
        height=3
    )
    label.grid(row=0, column=1)

    # Textbox
    entry = tk.Entry(mywindow, text="Calc")
    # action_with_arg=buttonPress(entry=entry)
    textbutton = tk.Button(mywindow, text="Text Box")

    entry.grid(row=1, column=1)
    # textbutton.grid(row=2, column=2)

    # Button
    button = tk.Button(mywindow, text='Clear', command=lambda: clear(entry))
    button.grid(row=2, column=1)

    list_of_buttons = list()

    # value = 9
    # for i in range(2, 5):
    #     for j in range(2, 5):
    #         # Create Frame
    #         frame = tk.Frame(
    #             master=mywindow,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j)
    #         # Create Button
    #         button = tk.Button(master=frame,
    #                 text=str(value),
    #                 width=2,
    #                 height=2,
    #                 bg="gray",
    #                 fg="black")
    #         button.grid(row=i, column=j)
    #         value -= 1
    #
    #         list_of_buttons.append(button)
    #

    # for bnt in list_of_buttons:
    #     bnt.config

    ################################################################
    button = tk.Button(
        text="+",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="+"))
    button.grid(row=2, column=7)

    button = tk.Button(
        text="-",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="-"))
    button.grid(row=2, column=8)
    ################################################################
    button = tk.Button(
        text="*",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="*"))
    button.grid(row=3, column=7)

    button = tk.Button(
        text="/",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="/"))
    button.grid(row=3, column=8)
    ################################################################
    button = tk.Button(
        text="**",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="**"))
    button.grid(row=4, column=7)

    button = tk.Button(
        text="R",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="R"))
    button.grid(row=4, column=8)

    button = tk.Button(
        text="8",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="8"))
    button.grid(row=2, column=5)

    button = tk.Button(
        text="5",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="5"))
    button.grid(row=3, column=5)

    button = tk.Button(
        text="2",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="2"))
    button.grid(row=4, column=5)

    button = tk.Button(
        text="9",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="9"))
    button.grid(row=2, column=6)

    button = tk.Button(
        text="6",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="6"))
    button.grid(row=3, column=6)

    button = tk.Button(
        text="3",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="3"))
    button.grid(row=4, column=6)

    button = tk.Button(
        text="0",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="0"))
    button.grid(row=5, column=5)

    button = tk.Button(
        text="7",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="7"))
    button.grid(row=2, column=4)

    button = tk.Button(
        text="4",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="4"))
    button.grid(row=3, column=4)

    button = tk.Button(
        text="1",
        width=2,
        height=2,
        bg="gray",
        fg="black", command=lambda: buttonEnterVal(entry, val="1"))
    button.grid(row=4, column=4)
    #####################################################################
    button = tk.Button(
        text="<----",
        width=6,
        height=2,
        bg="black",
        fg="cyan", command=lambda: backspace(entry))
    button.grid(row=3, column=1)
    #####################################################################
    button = tk.Button(
        text="=",
        width=2,
        height=2,
        bg="black",
        fg="yellow", command=lambda: readenry(entry))
    button.grid(row=5, column=7)
    #######################################################################
    button = tk.Button(
        text=".",
        width=2,
        height=2,
        bg="tan",
        fg="black", command=lambda: buttonEnterVal(entry, val="."))
    button.grid(row=5, column=6)

    mywindow.mainloop()
