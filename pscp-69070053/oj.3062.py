"""ค่าตั๋ว"""

def tricket():
    """ค่าตั๋ว"""

    age = int(input())
    stats = str(input())

    if age < 18 or stats == "s" or stats == "S":
        print("20")
    else:
        print("50")

tricket()
