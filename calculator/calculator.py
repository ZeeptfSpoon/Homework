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
            x = a + b
            logger.debug(x)
        elif function == "-":
            x = a - b
            logger.debug(x)
        elif function == "*":
            x = a * b
            logger.debug(x)
        elif function == "/":
            x = a / b
            logger.debug(x)
        elif function == "**":
            x = a ** b
            logger.debug(x)
        elif function == "sqrt":
            x = sqrt(a * b)
            logger.debug(x)


if __name__ == '__main__':
    calculate()


