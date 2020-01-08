def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def selector(a, b, c):
    if c == 1:
        return sum(a, b)
    elif c == 2:
        return subtract(a, b)
    elif c == 3:
        return multiply(a, b)
    elif c == 4:
        return divide(a, b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1 to add\n2 to subtract\n3 to multiply\n4 to divide")
    c = int(input())
    print(selector(a, b, c))


if __name__ == '__main__':
    main()
