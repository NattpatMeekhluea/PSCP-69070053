"""brickbridge"""

def main():
    """brickbridge"""

    brick_small = int(input())
    brick_large = int(input())
    goal = int(input())

    large_use = min(goal // 5, brick_large)
    remaining = goal - (large_use * 5)

    if brick_small >= remaining:
        print(remaining)
    else:
        print(-1)

main()
