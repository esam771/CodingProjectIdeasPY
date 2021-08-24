import random as r
from datetime import datetime as dt


def main():

    print('how many lines')
    lines = int(input())

    for x in range(lines):
        for y in range(4):
            for z in range(5):
                print(r.randint(0, 9), end="")
            print("", end=" ")
        print("")

    now = dt.now()
    print("\n   time:", now)


if __name__ == "__main__":
    main()
