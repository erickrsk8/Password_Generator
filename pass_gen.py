import random
import sys

# character types
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&^*\/"

try:
    # combine the character types
    use_for = lower_case + upper_case + number + symbols

    
    # user arguments as input for character length
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        length = int(sys.argv[1])
    else:
        length = 8

    # randomly generate the password
    password = "".join(random.sample(use_for, length))

    print(password)
except ValueError:
    print('Error: Invalid argument. Please use an integer.')
