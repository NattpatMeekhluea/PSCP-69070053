"""A-E-I-O-U"""

def main():
    """A-E-I-O-U"""

    #รับค่าตัวอักษรและกำหนดให้เป็นตัวพิมพ์เล็ก
    text = input().lower()

    #กำหนดตัวแปร vowels หรือตัวสระภาษาอังกฤษ และ count ให้เท่ากับ 0 5 ตัว
    vowels = ["a", "e", "i", "o", "u"]
    count = [0, 0, 0, 0, 0]

    #วนลูปตรวจสอบตัวอักษรที่รับเข้ามาว่าเป็นตัวสระหรือไม่แล้วให้เพิ่มค่า count ของตัวสระนั้นๆ
    for character in text:
        if  character in vowels:
            position = vowels.index(character)
            count[position] += 1

    #วนลูปตรวจสอบค่า count ของตัวสระแต่ละตัว ถ้ามีค่ามากกว่า 0 ให้แสดงผลลัพธ์ออกมา
    for position in range(5):
        if count[position] > 0:
            print(vowels[position], ":", count[position])

main()
