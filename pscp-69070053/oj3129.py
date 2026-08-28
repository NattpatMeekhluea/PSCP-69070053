"""วิเคราะห์ยอดขายร้านกาแฟ"""

def main():
    """วิเคราะห์ยอดขายร้านกาแฟ รวม,ขายสูง,ต่ำและยอดเฉลี่ยต่อวัน โดยปัดเศษทศนิยม 1 ต่ำแหน่ง"""
    cup = int(input())
    total = 0
    high_sell = -99999999
    low_sell = 99999999

    for _ in range(cup):
        sell = int(input())
        total += sell

        if high_sell < sell:
            high_sell = sell
        if low_sell > sell:
            low_sell = sell

    avg_per_day = total / cup

    print(total)
    print(high_sell)
    print(low_sell)
    print(f"{avg_per_day:.1f}")



main()
