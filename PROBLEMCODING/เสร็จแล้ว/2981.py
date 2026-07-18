"""ชื้อนามสกุล"""

name = input("name: ")
surname = input("surname: ")

print("Hello", name, surname)

nickname = name[:2] + surname[:2]

print(nickname)
