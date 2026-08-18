"""Elo"""

def main():
    """Elo"""

    ra = int(input())
    rb = int(input())
    player = input()
    if player == "A":
        EA = 1 / (1 + 10 **((rb - ra) / 400))
        print(f"{EA:.2f}")
    elif player == "B":
        EB = 1 / (1 + 10 **((ra - rb) / 400))
        print(f"{EB:.2f}")

main()

