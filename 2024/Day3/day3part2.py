#Day 3, Advent of code 2024
#import re to be able to use regex
import re

def calculate_multiplication_sum(data):
    # Flag to track wether multiplications are enabled or disabled
    enabled = True
    total_sum = 0
    #Removes newline from input data
    data = data.replace('\n', '') 

    #Uses regex to find all valid 'mul(x,y)' instructions in the data
    #(?<!?d)) is to ensure that 'mul' is not part of a larger number
    # ([?\d]+) is to capture one or more digits for both x and y
    # (?!\d) is to ensure the match is not part of a larger number
    matches = re.finditer(r"(?<!\d)(mul)\(([\d]+),([\d]+)\)(?!\d)", data)

    for match in matches:
        # Full match string
        instruction = match.group(0)
        # Starting position of the match in the string
        start_index = match.start()

        # Extracts all text before the current mul instruction
        prev_text = data[:start_index]
        # Finds the last occurance of "do()" and "don't()" before this mul
        do_index = prev_text.rfind("do()")
        dont_index = prev_text.rfind("don't()")
        # Determins whether multiplications should be enabled or disabled
        if do_index > dont_index:
            enabled = True
        elif dont_index > do_index:
            enabled = False

        if enabled:
            # Extracts the first number
            num1 = int(match.group(2))
            # Extracts the sescond number
            num2 = int(match.group(3))
            total_sum += num1 * num2

    return total_sum



try:
    with open('day3.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File 'input.txt' not found.")
    exit()

result = calculate_multiplication_sum(data)
print(f"The sum of enabled multiplications is: {result}")