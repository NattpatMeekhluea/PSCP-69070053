"""การตรวจสอบสระ"""

def checkchecki():
    """การตรวจสอบสระ"""
    vowel = str(input().lower())

    if vowel in ("a","e","i","o","u"):
        print("yes")
    else:
        print("no")

checkchecki()
