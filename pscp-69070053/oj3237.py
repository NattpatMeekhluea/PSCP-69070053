"""สามเหลี่ยม"""

def main():
    """สามเหลี่ยม"""

    limit = int(input())

    for row in range(1,limit + 1):
        for colum in range(1,row + 1):
            if colum == 1 or row == limit or colum == row:
                print("0",end="")
            else:
                print("1",end="")
        print()

main()
