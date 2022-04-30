

def main():
    print("format: 3x^5 -> 15x^4")
    print(separateFunction(str(input())))


def separateFunction(function):  # splits string input into tuple
    charArray = function.split("x^")
    try:
        term = (float(charArray[0]), "x^", float(charArray[1]))
    except:
        print("invalid input")
        exit()
    return derivative(term)


def derivative(term):  # basic power rule function
    coef = term[0] * term[2]
    deriv = str(coef) + term[1] + str(term[2]-1)
    return deriv


if __name__ == '__main__':
    main()
