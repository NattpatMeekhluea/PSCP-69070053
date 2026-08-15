"""กระต่ายอ้วน"""

def main():
    """กระต่ายอ้วน"""

    rabbit = int(input())

    haujad_num = 0
    haujadKon = -1
    haujad_name = ""

    for _ in range(rabbit):
        name,weight = input().split()
        weight = int(weight)

        if weight > 15:
            haujad_num += 1
        if weight > haujadKon:
            haujadKon = weight
            haujad_name = name

    print(haujad_num)
    print(haujad_name)

main()
