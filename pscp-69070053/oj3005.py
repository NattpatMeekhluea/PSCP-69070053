"""กระต่ายน้อยจ่ายตลาด"""

def main():
    """กระต่ายน้อยจ่ายตลาด"""

    carrot, cabbage, tomato = map(int, input().split())
    total = (carrot * 10) + (cabbage * 25) + (tomato * 3)

    print(total)

main()
