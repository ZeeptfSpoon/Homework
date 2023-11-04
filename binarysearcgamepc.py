from loguru import logger
import random


def binary_search_game():
    """
    method represent sim ple binary search between 2 parts of code
    :return: None
    """
    low = 0
    high = 100
    feedback = None
    logger.debug("Imagine a number between 0 and 100.")
    guess = random.randrange(0, 101)
    number = random.randrange(0, 101)
    logger.debug(number)
    while feedback != "c":

        logger.debug(f"Is your number{guess}?")
        if number > guess:
            feedback = "l"
            logger.debug("l")
            low = guess + 1
        elif number < guess:
            feedback = "h"
            logger.debug("h")
            high = guess - 1
        else:
            feedback = "c"
            logger.debug("c")
        guess = (low + high) // 2
    logger.debug("Congratulations! The number u imagined %s has been found." % guess)

    # while feedback != "c":
    #
    #     logger.debug(f"Is your number {guess} ?")
    #     feedback = input("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ")
    #
    #     if feedback == "h":
    #         high = guess - 1
    #
    #     elif feedback == "l":
    #         low = guess + 1
    #     guess = (low + high) // 2

    logger.debug("Congratulations! The number u imagined %s has been found." % guess)


if __name__ == '__main__':
    binary_search_game()
