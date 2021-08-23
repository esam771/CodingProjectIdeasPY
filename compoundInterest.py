

def main():

    print("initial money")
    quan = float(input())
    print("amount of trials")
    trials = int(input())
    print("percent gain")
    perc = float(input())
    print()

    for x in range(trials + 1):
        print(round(quan, 2))
        quan = quan * (perc / 100 + 1)


if __name__ == "__main__":
    main()
