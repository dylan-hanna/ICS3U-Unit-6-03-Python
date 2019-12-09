#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program finds the largest value


import random


def sum_of_numbers(list_of_numbers):
    # this function determines what the smallest number in the randomly generated list is

    smallest = list_of_numbers[0]
    for counter in list_of_numbers:
        if counter < smallest:
            smallest = counter
    return smallest


def main():
    # this function uses a list

    random_numbers = []
    biggest = 0

    # input
    print("The Numbers in the List are: ")
    for loop_counter in range(0, 9):
        single_number = random.randint(0, 1000)
        random_numbers.append(single_number)
        print("[{0}] ".format(single_number), end="")
    print("")

    biggest = sum_of_numbers(random_numbers)

    print("The smallest Number is: {0} ".format(biggest))


if __name__ == "__main__":
    main()
