"""การนับสระ"""

def main():
    """การนับสระ"""

    text = input().lower()
    vowel = "aeiou"
    count = 0

    for char in text:
        if char in vowel:
            count += 1
    print(count)

main()
