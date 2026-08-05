"""Temperature"""

def main():
    """Temperature"""

    #กำหนดตัวแปรและกำหนดcelให้เท่ากับ 0.0
    temperature = float(input())
    s_unit = input().upper()
    t_unit = input().upper()

    cel = 0.0


    # covert to cel
    if s_unit == "C":
        cel = temperature
    elif s_unit == "F":
        cel = (temperature - 32) * 5 / 9
    elif s_unit == "K":
        cel = temperature - 273.15
    elif s_unit == "R":
        cel = (temperature * 5 / 9) - 273.15

    #กำหนดตัวแปร result ให้เท่ากับ 0.0
    result = 0.0

    # convert to t_unit
    if t_unit == "C":
        result = cel
    elif t_unit == "F":
        result = (cel * 9 / 5) + 32
    elif t_unit == "K":
        result = cel + 273.15
    elif t_unit == "R":
        result = (cel + 273.15) * 9 / 5

    print(f"{result:.2f}")

main()
