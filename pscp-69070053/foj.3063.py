"""Saves password"""

def save_password():
    """Saves password"""

    character_password = str(input())
    number_password = int(input())

    corect_num_password = 4567
    corect_char_password ="H"

    if character_password ==  corect_char_password and number_password == corect_num_password:
        print("safe unlocked")
    elif character_password == "h" or number_password == corect_num_password:
        print("safe locked - change char")
    elif character_password == corect_char_password:
        print("safe locked - change digit")
    else:
        print("safe locked")
        
save_password()
