"""การตรวจสอบบัตรประชาชน"""

idcard = input()

if len(idcard) == 13:
    print("yes")
else:
    print("no")