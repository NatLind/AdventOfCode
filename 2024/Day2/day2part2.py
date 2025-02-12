#Day 2 part 2 , Advent of Code 2024

safe_count = 0

#Opens the textfile for reading
with open('day2.txt', 'r') as file:
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
            continue
        
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]

            increasing = all(1 <= (new_levels[j+1] - new_levels[j]) <= 3 for j in range(len(new_levels) -1))
            decreasing = all(1 <= (new_levels[j] - new_levels[j+1]) <= 3 for j in range(len(new_levels) -1))

            if increasing or decreasing:
                safe_count += 1
                break         

            

print(f'Number of safe reports: {safe_count}')
    
        