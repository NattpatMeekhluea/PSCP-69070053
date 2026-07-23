"""Season"""

def season():
    """Season"""
    month = int(input())
    day = int(input())

    if month <= 3:
        season_charge = "winter"
    elif month <= 6:
        season_charge = "spring"
    elif month <= 9:
        season_charge = "summer"
    else:
        season_charge = "fall"

    if month == 3 and day >= 21:
        season_charge = "spring"
    elif month == 6 and day >= 21:
        season_charge = "summer"
    elif month == 9 and day >= 21:
        season_charge = "fall"
    elif month == 12 and day >= 21:
        season_charge = "winter"

    print(season_charge)

season()
