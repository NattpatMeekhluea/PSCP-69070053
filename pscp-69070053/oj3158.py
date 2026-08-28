"""ผลรวมกำลัง 2"""

def main():
    """ผลรวมกำลัง 2"""

    num = int(input())
    total = 0

    for nu in range(1,num + 1):
        div = nu ** 2
        total += div

    print(total)

main()
