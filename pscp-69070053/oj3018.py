"""RectangleArea"""

def main():
    """RectangleArea"""

    a_x, a_y, a_width, a_height = map(int, input().split())
    b_x, b_y, b_width, b_height = map(int, input().split())

    overlap_width = max(
        0,
        min(a_x + a_width, b_x + b_width) - max(a_x,b_x)
    )
    overlap_height = max(
        0,
        min(a_y + a_height, b_y + b_height) - max(a_y,b_y)
    )

    overlap_area =  overlap_width * overlap_height
    if not overlap_area:
        print("no overlapping")
    else:
        print(overlap_area)
    
main()
