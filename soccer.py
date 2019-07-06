# encoding=utf8

# 2) The attached soccer.dat file contains the results from the English Premier League.
#   The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for 
# and against each team in that season (so Arsenal scored 79 goals against opponents, 
# and had 36 goals scored against them). Write a program to print the name of the 
# team with the smallest difference in ‘for’ and ‘against’ goals.

smallest = ["none", 1000]
file = open("soccer.dat", 'r')
for line in file:
    row = line.split()
    if (len(row) == 0):
        continue
    ateam = row[0].replace('.','') #to find which rows are teams
    if ateam.isdigit():
        against = row[6]
        scored = row[8]
        difference = abs(float(against)-float(scored))
        if difference < smallest[1]: #compare with smallest difference
            smallest = [row[1], difference]
print("Team Name: " + str(smallest[0]))
print("Smallest score difference: " + str(smallest[1]))

# Is the way you wrote the second program influenced by writing the first?

# Yes because the two prompts were similar. 
# I figured that the best runtime would be O(n) and so I did the work while iterating.
# The second program did simiarly