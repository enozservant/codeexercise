# encoding=utf8

"""2) The attached soccer.dat file contains the results from 
the English Premier League. The columns labeled ‘F’ and ‘A’ contain 
the total number of goals scored for and against each team 
in that season (so Arsenal scored 79 goals against opponents, 
and had 36 goals scored against them). Write a program to print the 
name of the team with the smallest difference in ‘for’ and ‘against’ goals.
"""

_scored_for = 'F'
_scored_against = 'A'
_first_column = "Team"
_team_infos = []
_table_columns = []
_smallest_diff = ["none", -1]


def parse_data(filename):
    file = open(filename, 'r')
    for line in file:
        line = line.replace('-', '')
        row = line.split()
        if not row:
            continue
        ateam = row[0].replace('.', '')
        if ateam.isdigit():
            row.pop(0)
            create_team(row)
        elif row[0] == _first_column:
            populate_columns(row)
    if _smallest_diff[1] != -1:
        print ("Team: " + _smallest_diff[0])
        print ("Smallest Diff: " + str(_smallest_diff[1]))


def populate_columns(row):
    for column in row:
        _table_columns.append(column)


def create_team(row):
    global _smallest_diff
    team_info = {}
    for column in range(0, len(_table_columns)):
        team_info[_table_columns[column]] = row[column]
    diff = abs(float(team_info[_scored_against]) -
               float(team_info[_scored_for]))
    if diff < _smallest_diff[1]:
        _smallest_diff = [team_info[_first_column], diff]
    elif _smallest_diff[1] == -1:
        _smallest_diff = [team_info[_first_column], diff]


if __name__ == '__main__':
    parse_data("soccer.dat")


""" Is the way you wrote the second program influenced by writing the first?
Yes because the two prompts were similar, but the datasets were different.
The first had missing data. To handle this, I filled in the missing data with a 0
to help with parsing the rest of the data in the dictionaries. The same with soccer. 
Because of the way that I parsed the first program, I did similarly for the second 
as I also used a similar technique.

I figured that the best runtime would be O(n) and so I did the work while iterating.
The second program did simiarly. But the first program takes longer than O(n) because
I iterate through each line to clean data. 
"""
