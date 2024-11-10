# infinite_write.py

# Code that will be written repeatedly to the output file
code_to_write = '''import random
import string
import time


'''

# Specify the file name where the code will be written
output_file = 'infinite_generated_code.py'

# Open the file in append mode and write the code in an infinite loop
while True:
    with open(output_file, 'a') as file:  # 'a' mode for appending
        file.write(code_to_write)
    print(f"Code written to {output_file}... (Press CTRL+C to stop)")
