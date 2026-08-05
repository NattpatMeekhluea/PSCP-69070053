"""Bill"""

def bill():
    """Bill"""
    food_bill = int(input())
    service_charge = food_bill *0.10

    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    subtotal = food_bill + service_charge
    vat_bill = subtotal *0.07
    total_bill = subtotal + vat_bill
    print(f"{total_bill:.2f}")

bill()
