import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:  # its default is True
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:  # meer_criteria still False or len of pwd is less than min_length
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:  # checks if new_char is in either digits or special
            has_number += True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:  # number included
            meet_criteria = has_number  # will return True
        if special_characters:  # has special char
            meet_criteria = meet_criteria and has_special  # both meet_criteria and has_special be true, to return true

    return pwd


min_length = int(input("Enter the minumum length: "))
has_number = input("Do you want to include number? (y/n) ").lower() == "y"
has_special = input("Do you want to include special characters? (y/n)").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generater password is", pwd)
