"""Colors"""

def main():
    """Colors"""
    first_color = input()
    second_color = input()

    if (first_color == "Red" and second_color == "Yellow"
    or first_color == "Yellow" and second_color == "Red"
    ):
        print("Orange")
    elif first_color == "Red" and second_color == "Red":
        print("Red")
    elif (first_color == "Red" and second_color == "Blue"
    or first_color == "Blue" and second_color == "Red"
    ):
        print("Violet")
    elif first_color == "Yellow" and second_color == "Yellow":
        print("Yellow")
    elif (first_color == "Yellow" and second_color == "Blue"
    or first_color == "Blue" and second_color == "Yellow"
    ):
        print("Green")
    elif first_color == "Blue" and second_color == "Blue":
        print("Blue")
    else:
        print("Error")

main()
