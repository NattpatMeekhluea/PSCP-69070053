"""VowelbutNoCount"""

def main():
    """VowelButNoCount"""

    text = input().lower()
    vowelcount = 0

    for ch in text:
        if ch in "aeiou":
            vowelcount += 1
    print(vowelcount)

main()
