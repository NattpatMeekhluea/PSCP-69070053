"""ผลการสอบ"""

def main():
    """ผลการสอบ"""

    work_score = int(input())
    midterm = int(input())
    final = int(input())

    work_pass = work_score >= 5
    midterm_pass = midterm >= 20
    final_pass = final >= 25

    if work_pass and midterm_pass and final_pass:
        print("pass")
    else:
        print("fail")
main()
