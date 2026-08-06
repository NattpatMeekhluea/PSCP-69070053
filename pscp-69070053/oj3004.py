"""หาระยะทางระหว่างจุด 3D"""

import math

def main():
    """หาระยะทางระหว่างจุด 3D"""
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"{distance:.2f}")

main()
