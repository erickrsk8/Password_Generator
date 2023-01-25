import random
import sys

# character types
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&^*\/"

# combine the character types
use_for = lower_case + upper_case + number + symbols

# user arguments as input for character length
length = int(sys.argv[1])

# randomly generate the password
password = "".join(random.sample(use_for, length))

print(password)
