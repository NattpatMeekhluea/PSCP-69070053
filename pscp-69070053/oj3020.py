"""Coke Promotion"""

def main():
    """Calculate the minimum price for Coke."""
    normal_price = int(input())
    caps = int(input())
    promotion_price = int(input())
    amount = int(input())

    if not caps or not amount:
        total = amount * normal_price
    else:
        promotion = (amount - 1) // caps
        normal = amount - promotion
        total = (normal * normal_price) + (promotion * promotion_price)

    print(total)

main()
