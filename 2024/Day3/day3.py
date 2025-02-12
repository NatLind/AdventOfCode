#Day 3, Advent of code 2024
#import re to be able to use regex
import re

#Sets total sum to 0
total_sum = 0

with open ('day3.txt', 'r') as file:
    for line in file:
        #reads through lines and finds all valid  mul(x,y)
        match = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)

        for x,y in match:
            total_sum += int(x) * int(y)

print(f'The total sum is {total_sum}')


        


