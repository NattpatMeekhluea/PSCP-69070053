"""สลับหมายเลข"""

def main():
    """สลับหมายเลข"""
    number = int(input())
    optor = input()

    tens = number // 10
    ones = number % 10
    reserved = ones * 10 + tens

    if optor == "+":
        result = number + reserved
    else:
        result = number * reserved

    print(number, optor, reserved, "=", result)

main()
