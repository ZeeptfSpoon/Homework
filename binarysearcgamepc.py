from loguru import logger
import random


def binary_search_game():
    """
    method represent simple binary search between 2 parts of code
    :return: None
    """
    low = 0
    high = 100
    feedback = None

    logger.debug("Imagine a number between 0 and 100.")
    guess = random.randrange(0, 101)  # random of 1rst guess
    number = random.randrange(0, 101)  # our random number
    logger.debug(number)  # this guy right here to check is there any mistakes in search

    while feedback != "c":

        logger.debug(f"Is your number{guess}?")
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


if __name__ == '__main__':
    binary_search_game()
