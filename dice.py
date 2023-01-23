# dice.py


def parse_input(input_string):
    """Return `input string` is an integer number between 1-6. 

    Check if `input string` is an interger number between 1-6.
    If so, return integer with the same value. Otherwise, tell 
    the user to enter a valid number and quit the program.
    """
    if Input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)

    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
# ~~~ App's main code block ~~~
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
