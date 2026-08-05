"""Han Zeb"""


def main():
    """Han Zeb."""
    number = int(input())
    start_number = number - (number % 10)

    for current_number in range(start_number, -1, -10):
        print(current_number, end=" ")


main()
