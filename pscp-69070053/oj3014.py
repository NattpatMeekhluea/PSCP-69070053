"""Milk"""

def main():
    """Milk"""

    milk_price  = int(input())
    lids_requried = int(input())
    promotion_milk = int(input())
    customer_money = int(input())

    milk_bottle = customer_money // milk_price
    total_milk = milk_bottle
    lids = milk_bottle

    if lids_requried:
        while lids >= lids_requried:
            new_milk = (lids // lids_requried) * promotion_milk
            total_milk += new_milk
            lids = (lids % lids_requried) + new_milk

    print(total_milk)

main()
