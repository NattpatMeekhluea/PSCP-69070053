"""จำนวนสระ"""

def main():
    """จำนวนสระ"""

    text = int(input())
    count = 0

    for _ in range(text):
        vowel = input().upper()
        if vowel in "AEIOU":
            count += 1
    print(count)

main()
