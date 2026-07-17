"""Colors"""

def main():
    """Colors"""
    firstcolors = input()
    secondcolors = input()

    if (firstcolors == "Red" and secondcolors == "Yellow"
    or firstcolors == "Yellow" and secondcolors == "Red"
    ):
        print("Orange")
    elif (firstcolors == "Red" and secondcolors == "Red"
    or firstcolors == "Red" and secondcolors == "Red"
    ):
        print("Red")
    elif (firstcolors == "Red" and secondcolors == "Blue"
    or firstcolors == "Blue" and secondcolors == "Red"
    ):
        print("Violet")
    elif (firstcolors == "Yellow" and secondcolors == "Yellow"
    or firstcolors == "Yellow" and secondcolors == "Yellow"
    ):
        print("Yellow")
    elif (firstcolors == "Yellow" and secondcolors == "Blue"
    or firstcolors == "Blue" and secondcolors == "Yellow"
    ):
        print("Green")
    elif (firstcolors == "Blue" and secondcolors == "Blue"
    or firstcolors == "Blue" and secondcolors == "Blue"
    ):
        print("Blue")
    else:
        print("Error")

main()
