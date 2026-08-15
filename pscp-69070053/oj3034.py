"""Port"""

def main():
    """Port"""
    customer_in_line, line_port = map(int, input().split())

    queues = [0] * line_port


    for _ in range(customer_in_line):
        line_number = int(input())
        queues[line_number - 1] +=1

    minimum_que = min(queues)
    remain_people = customer_in_line -(minimum_que * line_port)

    print(remain_people)

main()
