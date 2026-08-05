"""suprising"""

def main():
    """suprising"""

    total_score = float(input())
    max_score = float(input())

    minimum_score = max(0, total_score - (max_score * 2))
    difference = max_score - minimum_score

    if difference > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
