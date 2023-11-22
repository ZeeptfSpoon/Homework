from loguru import logger
import random


def binary_search_game(upper_border: int):
    """
    method represent simple binary search between 2 parts of code
    :param: upper_border (int) - Upper value for random  method
    upper_border has to be > 0
    :return: None
    """
    low = 0
    high = upper_border
    feedback = None

    if upper_border is not None and upper_border > 0 :
        logger.debug("Imagine a number between 0 and 100.")
        guess = random.randrange(0, 101)  # random of 1rst guess
        number = random.randrange(0, 101)  # our random number
        logger.debug(number)  # this guy right here to check is there any mistakes in search
        logger.debug("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ")
        while feedback != "c":

            logger.debug(f"Is your number {guess}?")
            if number > guess:
                feedback = "l"
                logger.debug("l")  # like dialogue between humans
                low = guess + 1
            elif number < guess:
                feedback = "h"
                logger.debug("h")
                high = guess - 1
            else:
                feedback = "c"
                logger.debug("c")
            guess = (low + high) // 2  # binary search function

        logger.debug("Congratulations! The number u imagined %s has been found." % guess)
    elif upper_border <= 0:
        logger.error("please set upper_border higher than 0")
    else:
        logger.error("Please set upper_border")


if __name__ == '__main__':
    binary_search_game(upper_border="1")