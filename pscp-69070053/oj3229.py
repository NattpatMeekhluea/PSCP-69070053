"""ระบบคิดคะแนนเกมออนไลน์"""

def main():
    """ระบบคิดคะแนนเกมออนไลน์ """

    base_score = int(input())
    bonus_score = int(input())
    play_streak  = int(input())

    if play_streak >= 3:
        total_score = 1.5 * (base_score + bonus_score)
    else:
        total_score = base_score + bonus_score

    if total_score >= 1500:
        scoreboard = 5
    elif total_score >= 1000:
        scoreboard = 4
    elif total_score >= 500:
        scoreboard = 3
    elif total_score >= 200:
        scoreboard = 2
    else:
        scoreboard = 1

    if scoreboard == 5 and play_streak >= 7:
        speicalscore = 99
    elif scoreboard == 4 and bonus_score > 300:
        speicalscore = 88
    else:
        speicalscore = 0

    print(int(total_score))
    print(scoreboard)
    print(speicalscore)

main()
