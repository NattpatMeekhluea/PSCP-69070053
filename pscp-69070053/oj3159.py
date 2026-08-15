""""Factorial"""

def main():
    """Factorial"""

    first_num = int(input())
    result = 1

    for num in range(1,first_num +1):
        result = result * num
    print(result)

main()
