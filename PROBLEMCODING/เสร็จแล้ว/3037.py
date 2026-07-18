"""ค่ามากที่สุด"""

def main():
    """ค่ามากที่สุด"""
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    maxend = n1
    if n2 > maxend:
        maxend = n2
    if n3 > maxend:
        maxend = n3

    print(maxend)
main()
