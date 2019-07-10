# encoding=utf8

""" 1) In the attached file (w_data.dat), you’ll find daily weather data.   
Download this text file, then write a program to output the day number 
(column one) with the smallest temperature spread (the maximum temperature 
is the second column, the minimum the third column).
"""

_every_day_info = []
_columns = []
_column_width = []
_first_column = "Dy"
_max_column = "MxT"
_min_column = "MnT"
_lowest_spread = [0, -1]


def populate_info(file_name):
    file = open(file_name, 'r')
    for line in file:
        row = line.split()
        if not row:
            continue
        if row[0].isdigit():
            parse_row(line)
        elif row[0] == _first_column:
            populate_columns(line)
    if _lowest_spread[1] != -1:
        print("Day: " + str(_lowest_spread[0]))
        print("Lowest Spread: " + str(_lowest_spread[1]))


def populate_columns(line):
    # While putting all column titles in _columns,
    # find each column length to help with cleaning data
    global _columns
    global _column_width
    _columns = line.split()
    line = line.strip()
    for curr in range(0, len(_columns)-1):
        if curr-1 != len(_columns):
            next_loc = line.find(_columns[curr+1])
            spaces = next_loc
            line = line[next_loc:]
            _column_width.append(spaces)
        else:
            _column_width.append(len(_columns[curr]))


def parse_row(line):
    # Parses each line to clean data of empty columns
    # by entering in a '0' in its place to match
    # amount of columns
    global _column_width
    line = line.strip()
    if int(line[0]+line[1]) < 10:
        line = " " + line

    curr_index = 0
    curr_column = 0
    for width in _column_width:
        dataexists = False
        for length in range(0, int(width)-1):
            if line[curr_index+length] != ' ':
                dataexists = True
                break
        if not dataexists:
            line = line[0:curr_index] + '0' + line[curr_index+1:]
        curr_index += int(width)
    line = line.replace('*', '')
    check_day(line.split())
    # print line
    # this line can be used to help see what I did in this code


def check_day(arr_of_data):
    # Creates a dictionary for a day according to each column
    # while checking if it is the lowest spread
    global _lowest_spread
    day_info = {}
    for index in range(0, len(_columns)):
        day_info[_columns[index]] = arr_of_data[index]
    _every_day_info.append(day_info)
    diff = abs(float(day_info[_max_column]) - float(day_info[_min_column]))
    if diff < _lowest_spread[1]:
        _lowest_spread = [day_info[_first_column], diff]
    elif _lowest_spread[1] == -1:
        _lowest_spread = [day_info[_first_column], diff]

if __name__ == '__main__':
    populate_info("w_data (5).dat")

# Enoch Hang
