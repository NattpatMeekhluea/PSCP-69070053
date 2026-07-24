"""Pass/NotPass"""

def passnotpass():
    """Pass/NotPass"""

    midterm_score = int(input())
    finalterm_score = int(input())
    result = midterm_score + finalterm_score

    if midterm_score + finalterm_score >= 50:
        print(result)
        print("pass")
    elif midterm_score + finalterm_score <= 50:
        print(result)
        print("fail")

passnotpass()
