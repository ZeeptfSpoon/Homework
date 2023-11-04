def binary_search_human():
    low = 0
    high = 100
    feedback= None
    print("Imagine a number between 0 and 100.")

    while feedback != "c":
        guess = (low + high) // 2
        print("Is your number ",guess,"?")
        feedback = input("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ")

        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1

        elif feedback != "c":
            print("Please enter 'h', 'l', or 'c' for feedback.")

    print(f"Congratulations! The number u imagined {guess} has been found.")
binary_search_human()