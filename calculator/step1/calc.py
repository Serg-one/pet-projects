def add(a, b):
    """
    Adding two numbers
    :param a: first addend
    :param b: second addend
    :return: sum
    """
    return a + b


def subtract(a, b):
    """
    Take away a number from another to calculate the difference
    :param a: minuend
    :param b: subtrahend
    :return: difference
    """
    return a - b


def divide(a, b):
    """
    Divide two numbers
    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    return a / b


def multiply(a, b):
    """
    Multiply two numbers
    :param a: multiplicand
    :param b: multiplier
    :return: product
    """
    return a * b


def main():
    # No additional checks for inputs
    a = int(input("Input first operand (must be integer): "))
    b = int(input("Input second operand (must be integer): "))
    c = input("Input operation (+, -, /, *): ")

    match c:
    # Python 3.10 and above
        case '+':
            print(add(a, b))
        case '-':
            print(subtract(a, b))
        case '*':
            print(multiply(a, b))
        case '/':
            print(divide(a, b))
        case other:
            print('Invalid operation')


if __name__ == '__main__':
    main()