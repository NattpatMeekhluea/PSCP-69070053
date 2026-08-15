"""จำนวนสระ"""

def main():
    """จำนวนสระ"""

    amount  = int(input())
    count = 0

    for _ in range(amount):
        vowel = input().upper()
        if vowel in "AEIOU":
            count += 1
    print(count)

main()
