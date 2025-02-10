#Day 2, Advent of Code 2024

safe_count = 0

#Opens the textfile for reading
with open ('day2.txt', 'r') as file:
    for line in file:
        #Convert each line into a list of int
        levels = list(map(int, line.strip().split()))
        # Check if the report is gradually increasing
        increasing = all(1 <= (levels[i+1] - levels[i]) <= 3 for i in range(len(levels)-1))
        #Check if the report is gradually decreasing
        decreasing = all(1 <= (levels[i] - levels[i+1]) <= 3 for i in range(len(levels)-1))

        #If report is either increasing or decreasing, count it as safe
        if increasing or decreasing:
            safe_count += 1

print(f'Antal säkra rapporter: {safe_count}')
    
        