"""แลกตัง"""

def main():

    """แลกตัง"""
    money = int(input())

    c10 = money // 10
    money %= 10
    c5 = money // 5
    money %= 5
    c2 = money // 2
    money %= 2
    c1 = money // 1

    print("10","=",c10)
    print("5","=",c5)
    print("2","=",c2)
    print("1","=",c1)

main()
