"""AR"""

def main():
    """AR"""
    r, x, y = map(int, input().split())

    eyes_point = (x**2)+(y**2)
    circle_radius = r**2

    if eyes_point < circle_radius:
        print("IN")
    elif eyes_point == circle_radius:
        print("ON")
    else:
        print("OUT")

main()
