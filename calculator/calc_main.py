from loguru import logger

from math import sqrt


def calculate():
    """calculator in which you can do easy math functions
        if sqrt(square root)
        :return: None
    """

    function = None

    if function != "C":  # when user will set "=" the cycle will end
        a = float(input("first number please "))
        function = input("insert yours function ")
        b = float(input("second number please "))
        if function == "+":
            x = summ(a, b)
            logger.debug(x)
        elif function == "-":
            x = margin(a, b)
            logger.debug(x)
        elif function == "*":
            x = multiply(a, b)
            logger.debug(x)
        elif function == "/":
            x = divide(a, b)
            logger.debug(x)
        elif function == "**":
            x = power(a, b)
            logger.debug(x)
        elif function == "sqrt":
            x = square(a)
            logger.debug(x)


def summ(a=None, b=None):  # PEP8
    """
    method perform multiplication of two numbers
    :param a:
    :param b:
    :return: summ a+b or None
    """
    if a and b is not None:
        return a + b


def margin(a=None, b=None):
    """
    method perform margin between two numbers
    :param a: 
    :param b: 
    :return: marg a-b or None
    """
    if a and b is not None:
        return a - b


def multiply(a=None, b=None):
    """
    method perform multiplication between two numbers
    :param a:
    :param b:
    :return: marg a*b or None
    """
    if a and b is not None:
        return a * b


def divide(a=None, b=None):
    """
    method perform divide between two numbers
    :param a:
    :param b:
    :return: marg a / b or None
    """
    if a and b is not None and b != 0:
        return a / b

def power(a=None, b=None):
    """
    method perform a to the power of b
    :param a:
    :param b:
    :return: marg a ** b or None
    """
    if a and b is not None:
        return a ** b


def square(a=None):
    """
    method perform square root from number
    :param a:
    :return: sqrt(a) or None
    """
    if a is not None:
        return sqrt(a)

# ent.split(+)
if __name__ == '__main__':
    calculate()



