"""yoo"""

def main():
    """yoo"""

    x_1 = int(input())
    y_1 = int(input())
    radius_1 = int(input())
    x_2 = int(input())
    y_2 = int(input())
    radius_2 = int(input())

    distance_squared = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
    radius_sum_squared = (radius_1 + radius_2) ** 2

    if distance_squared < radius_sum_squared:
        print("overlapping")
    else:
        print("no overlapping")

main()
