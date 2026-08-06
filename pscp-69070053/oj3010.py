"""Quadrant"""

def main():
    """Find the position of a point"""
    x_coord = int(input())
    y_coord = int(input())

    if not x_coord and not y_coord:
        print("O")
    elif not y_coord:
        print("X")
    elif not x_coord:
        print("Y")
    elif x_coord > 0 and y_coord > 0:
        print("Q1")
    elif x_coord < 0 < y_coord:
        print("Q2")
    elif x_coord < 0 and y_coord < 0:
        print("Q3")
    else:
        print("Q4")

main()
