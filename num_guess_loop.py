#!/usr/bin/env python3
# Created By: Joyceline
# Created on: November 18, 2026
# This program asks the user for a number between 0 and 9
# and checks if the input is valid or not. If the input is valid,
# it will display the number back to the user in a loop and break.

import random


def main():
    # a number between 0 and 9
    random_variables = random.randint(0, 9)

    while True:
        user_number_str = input("Enter a guess number :")
        try:
            user_number_int = int(user_number_str)
            if user_number_int < 0:
                print(
                    "{} is a negative integer that is not in between 0 and 9.".format(
                        user_number_str
                    )
                )
                print("Please enter a valid integer between 0 and 9.")
                break
        except ValueError:
            print(f"{user_number_str} is not an integer")
            break

        if user_number_int == random_variables:
            print("You guess the correct answer {}".format(random_variables))
            print("GOOD JOB!!!")
            break
        else:
            print("You got it wrong.")
            print("The correct answer is {}.".format(random_variables))
            break


if __name__ == "__main__":
    main()
