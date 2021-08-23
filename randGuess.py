import random
import math


def main():

    notf = True
    guesses = 0

    print("Enter Num Range 0-x")
    bound = int(input())

    rand = round(random.uniform(0, bound), 0)

    if rand < 1:
        quit()

    print("Enter guess, 1-x")
    # print(rand)

    while notf:

        guesses += 1
        guess = int(input())

        if guess > rand:
            print("too high")

        elif guess < rand:
            print("too low")

        else:
            print("correct guess! \n")
            notf = False

    print("guess count: ", guesses)
    print("\nAverage Guesses Using binary Search:")

    if bound >= 0:
        print("upper bound", bound, "->", round(math.log(bound, 2), 3))

    print("\nHow a computer would find it")

    binarysearch(rand, bound)


def binarysearch(rand, upperbound):

    lowerbound = 0
    guesses = 0
    nfound = True

    while nfound and guesses < 25:
        guesses += 1
        print(lowerbound, " ", upperbound, " ", guesses)

        if rand > (upperbound + lowerbound) / 2:
            lowerbound = int((upperbound + lowerbound) / 2)
            # round down for setting lower bound

        elif rand < (upperbound + lowerbound) / 2:
            upperbound = int(math.ceil((upperbound + lowerbound) / 2))
            # round up for setting upper bound

        else:
            nfound = False
            # found, end condition

    print("\ncomputer found in", guesses, "guesses")


if __name__ == "__main__":
    main()
