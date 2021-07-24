
def main():

    print("product to find factor of (must be number)")
    product = int(input())

    for x in range(1, product):
        if (product % x == 0) & (x < product/2):
            print(x, ' ', int(product/x))


if __name__ == "__main__":
    main()
