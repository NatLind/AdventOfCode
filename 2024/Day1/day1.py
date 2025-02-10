
#Day 1 part 1, advent of code 2024

#Opens textfile for reading
with open ('day1.txt', 'r') as lists:
    lines = lists.readlines()
    #Reads all lines from the file
    
#Empty lists to store numbers from  the textfile
left_list=[]
right_list=[] 

#Loops through each line
for line in lines:
    #Splits lines into two int
    left, right = map(int, line.strip().split())
    #Appends the int to their lists
    left_list.append(left)
    right_list.append(right)

#Sorts lists into ascending order
left_list.sort()
right_list.sort()

#Sets value to 0
total_distance = 0

#Iterate over both lists at the same time with zip
for left, right in zip(left_list, right_list):
    #Adds the absolute difference to total_distance
    total_distance += abs(left - right)

print(f'The distance is {total_distance} .')