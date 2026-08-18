"""การเพิ่ม/ลด"""

def main():
    """การเพิ่ม/ลด"""

    first = float(input())
    sec = float(input())
    third = float(input())

    if first < sec < third:
        print("increasing")
    elif first > sec > third:
        print("decreasing")
    else:
        print("neither")


main()
