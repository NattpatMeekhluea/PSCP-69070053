"""ค่าน้อยที่สุด (4 ค่า)"""

def main():
    """ค่าน้อยที่สุด (4 ค่า)"""

    x = int(input())
    low_score = 0

    for mun in range(x):
        score = int(input())
        if not mun or score < low_score:
            low_score = score
    print(low_score)

main()
