#Day 1 part 2, Advent of Code 2024

#Importing Counter
from collections import Counter

#Opens textfile for reading
with open ('day1.txt', 'r') as lists:
    lines = lists.readlines()
    #Reads all lines from the file

#Empty lists to store numbers from  the textfile
left_list = []
right_list = []

#Loops through each line
for line in lines:
    #Splits lines into two int
    left, right = map(int, line.strip().split())
    #Appends the int to their lists
    left_list.append(left)
    right_list.append(right)

#Counts occurences of each number in right_list
right_counter = Counter(right_list)

#Sets score to 0
total_similarity_score = 0

#Loops through each number in the left list
for left in left_list:
    #Adds the result of the number times its count to the total score
    total_similarity_score += left * right_counter[left]

print(f'Total similarity score is {total_similarity_score}')