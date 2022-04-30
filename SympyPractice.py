from sympy import *
# requires sympy, 'pip install sympy' in terminal
# https://docs.sympy.org/latest/tutorial/index.html#tutorial
x = symbols("x")
expr = cos(x) - sin(x) - x**4 + 1  # enter function here


def main():
    print("enter val of x")
    val = input()
    print("f(x) = ", evaluate(val))
    print("f'(x) = ", evaluateDeriv(val))


def evaluate(y):
    return expr.subs(x, y)


def evaluateDeriv(y):
    deriv = diff(expr, x)
    return deriv.subs(x, y)  # magic


if __name__ == '__main__':
    main()
