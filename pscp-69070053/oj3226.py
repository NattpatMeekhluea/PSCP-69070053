"""Inflation"""

def main():
    """Inflation"""

    price = input()
    years = int(input())

    if "." in price:
        baht,satang = price.split(".")
    else:
        baht = price
        satang = ""

    satang = (satang + "00")[:2]
    price = int(baht)* 100 + int(satang)

    for _ in range(years):
        increase = price * 381 // 10000
        price += increase

    baht = price // 100
    satang = price % 100
    print(f"{baht}.{satang:02d}")

main()
