"""ค่าน้อยที่สุด"""

def main():
    """ค่าน้อยที่สุด"""
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    minend = n1
    if n2 < minend:
        minend = n2
    if n3 < minend:
        minend = n3

    print(minend)
main()
