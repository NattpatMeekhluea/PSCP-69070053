"""กระต่ายน้อยล้อมรั้วลวดหนาม"""

def main():
    """กระต่ายน้อยล้อมรั้วลวดหนาม"""
    width,lenght,layer = map(int,input().split())
    pice = int(input())

    wire_length = 2*(width + lenght) * layer
    total = wire_length * pice

    print(wire_length)
    print(total)

main()
