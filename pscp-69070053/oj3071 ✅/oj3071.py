"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())

    count = 0
    for number in range(A, B + 1):
        if number % d == r:
            count += 1

    print(count)

main()
