"""Calculator"""

def main():
    """Calculator"""
    number = int(input())
    presses = 0

    for current in range(1, number + 1):
        presses += len(str(current))

    if number > 1:
        presses += number

    print(presses)

main()
