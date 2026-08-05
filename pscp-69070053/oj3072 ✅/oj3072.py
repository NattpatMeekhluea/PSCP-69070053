"""A-E-I-O-U"""

def main():
    """A-E-I-O-U"""
    
    #รับค่าตัวอักษรและกำหนดให้เป็นตัวพิมพ์เล็ก
    text = input().lower()

    for vowel in "aeiou":
        count = text.count(vowel)
        if count > 0:
            print(vowel, ":", count)

main()
 