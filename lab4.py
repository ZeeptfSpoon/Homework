# practical exercises from university lab2
# Global Constants Values:
list_of_users = ('Admin', 'Tymothy', 'Michael', 'Andrew', 'Daniel')
dictionary_of_figures = {"3": 'Triangle', "4": 'Square', "5": 'Pentagon', "6": 'Hexagon'}
list_of_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


# 1st exercise
# def Site_entrance(data: tuple):
#     """
#     method represents easy algorythm of greating users
#     return: hi user or error
#     """
#     name = input("Login please: ")
#     if name == 'Admin':
#         print("Hello Admin, I hope you’re well.")
#         if len(data) <= 1:
#             print("We need to find some users!")
#     elif name in data:
#         print(f"Hello ", name, ", thank you for logging in again.")
#     else:
#         print("Wrong name")
#
#
# if __name__ == '__main__':
#     Site_entrance(list_of_users)

# 2nd exercise

# def name_of_geometric_figure(diction: dict):
#     """
#     Method represents easy search between number of edges and figure
#     Algorythm: User inserts number of edges
#                 computer checks it in dict
#                 output: name of figure
#     """
#     nm_eg = input("Please insert number of edges: ")
#     print (diction[nm_eg])
# if __name__ == '__main__':
#     name_of_geometric_figure(dictionary_of_figures)

def ending_to_num(data: tuple):
    if "1" in data:
        print("1" + "st")
    if "2" in data:
        print("2" + "nd")
    if "3" in data:
        print("3" + "rd")
    for num in range(3,len(data)):
        print(data[num]+"th")
# def ending_to_num(data: tuple):
#
#     for num in range(0,len(data)):
#         if "1" in data:
#             print("1" + "st")
#         elif "2" in data:
#             print("2" + "nd")
#         elif "3" in data:
#             print("3" + "rd")
#         else:
#             print(data[num]+"th")


if __name__ == '__main__':
    ending_to_num(list_of_numbers)


