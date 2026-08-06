"""ink"""

import math


def main():
    """ink"""
    #สร้างตัวแปรสองตัวโดยใช้ map เพื่อให้ input เป็น int และใช้ split เพื่อแยกตัวเลขสองตัวในบรรทัดเดียวกัน
    ink_spread, house = map(int, input().split())
    
    #วนลูปตามจำนวนบ้านที่รับเข้ามา
    for _ in range(house):
        x, y = map(int, input().split())
        
        distance = (x ** 2 )+ (y ** 2)
        time = (3.1416 * distance) / ink_spread
        #ใช้ math.ceil เพื่อปัดเศษขึ้นเป็นจำนวนเต็ม  
        answer = math.ceil(time)
        print(answer)

main()
