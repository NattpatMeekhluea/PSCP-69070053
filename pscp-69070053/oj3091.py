"""Professor"""

def main():
    """Professor"""

    name = str(input())
    surname = str(input())
    year_born = int(input())

    first_latter_surname = surname[0]
    if year_born >= 0 <= 10000:
        print(name + "",first_latter_surname,".","was born in",year_born)
main()
