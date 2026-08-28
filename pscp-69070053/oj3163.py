"""สินค้าส่งออก"""

def main():
    """สินค้าส่งออก"""

    num = int(input())
    total = 0
    eve = 0
    odda = 0

    for _ in range(num):
        product = int(input())
        total += product

        if product % 2:
            odda += 1
        else:
            eve += 1

    print("SUM",(total))
    print("EVEN",(eve))
    print("ODD",(odda))

main()
