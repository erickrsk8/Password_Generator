# This script is used to setup the passgen cli

import os

# Find path to passgen.py
passgen_path = os.path.abspath("pass_gen.py")

#Get path to users config
config_path = os.environ['HOME'] + '/.' + os.environ['SHELL'].split('/')[-1] + 'rc'

# define the passgen function for rc
passgen_function = f"""
passgen () {{
    python {passgen_path} $1
}}
"""

# add the passgen function to the users shell config
with open(config_path, "a") as f:
    f.write(passgen_function)

print("The passgen function has been added to your shell config file.")
