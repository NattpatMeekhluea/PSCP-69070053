"""[LEARNING LOGS] ปราสาท"""

import math

def main():
    """[LEARNING LOGS] ปราสาท"""

    start_spot = int(input())

    r = int(math.sqrt(start_spot - 1)) + 1
    k = start_spot - (r - 1) ** 2

    if k % 2:
        print(2 * (r - 1))
    else:
        print(2 * r - 3)

main()
