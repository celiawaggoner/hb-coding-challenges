def print_digits(num):
    """Given an integer, print the digits of the number in reverse order."""

    while not num % 10 == num:

        next_digit = num % 10
        print next_digit
        num = (num - next_digit) / 10

    print num