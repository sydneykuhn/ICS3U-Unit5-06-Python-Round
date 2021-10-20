#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program rounds a number


def round_number(f_user_number, i_round_by):
    # round number

    # process
    temp = (f_user_number[0] * (10 ** i_round_by)) + 0.5
    temp = int(temp)
    temp = temp / (10 ** i_round_by)

    f_user_number[0] = temp


def main():
    # this function gets the user input
    i_user_number_list = []

    # input
    s_user_number = input("Enter the number you want to round : ")
    s_round_by = input("Enter how many decimal places you want to round by : ")

    try:
        f_user_number = float(s_user_number)
        i_user_number_list.append(f_user_number)
        i_round_by = int(s_round_by)
        # call function
        round_number(i_user_number_list, i_round_by)
        print("\nThe rounded number is {0}.".format(i_user_number_list[0]))
    except Exception:
        print("\nInvalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
