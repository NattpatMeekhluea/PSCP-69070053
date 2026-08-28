"""โรงแรมกลางกรุง ไม่มีชั้น 13"""

def main():
    """โรงแรมกลางกรุง ไม่มีชั้น 13"""

    num = str(input())

    floor = num[0] + num[-1]
    room = num[3] + num[4]

    
    
    if int(num[0]) > 5:
        floor1 = 9 
    elif int(num[1]) > 5:
        floor1 = 10
    elif int(num[2]) > 5:
        floor1 = 11
    elif int(num[3]) > 5:
        floor1 = 12
    elif int(num[0]) > 5:
        floor1 = 14
    else:
        floor1 = 13
    
    if int(num[0]) + int(num[4]) >5:
        floor2 = 1
    elif int(num[1]) * int(num[3]) >5:
        floor2 = 2
    else:
        floor2 = 0
    print(floor2)

main()
    