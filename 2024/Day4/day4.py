#Advent of code 2024, day 4


def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    #Iterates through each row
    for r in range(rows):
        #iterates through each column
        for c in range(cols):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:  # Alla 8 riktningar
                # Check if we are within the grid boundaries when checking for XMAS
                if r + 3*dr >= 0 and r + 3*dr < rows and c + 3*dc >= 0 and c + 3*dc < cols: 
                    word = ''
                    # Builds the letter
                    for i in range(4):
                        word += grid[r + i*dr][c + i*dc]
                    if word == "XMAS":
                        count += 1
    return count

# Reads file and creates a grid
grid = []
with open('day4.txt', 'r') as file:
    for line in file:
        # Creates a list of chars for each lines
        grid.append(list(line.strip())) 

xmas_count = find_xmas(grid)
print(f"XMAS can be found {xmas_count} times.")

