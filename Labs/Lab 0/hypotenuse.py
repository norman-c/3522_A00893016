import math


def calculatehypotenuse(a, b):
    return math.sqrt(a * a + b * b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calculatehypotenuse(a, b))


if __name__ == '__main__':
    main()
