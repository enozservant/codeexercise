# encoding=utf8

# 1) In the attached file (w_data.dat), you’ll find daily weather data.   
# Download this text file, then write a program to output the day number 
# (column one) with the smallest temperature spread (the maximum temperature 
# is the second column, the minimum the third column).

normalday = [0,1000]
file = open("w_data (5).dat", 'r')
for line in file:
    row = line.split()
    if (len(row) == 0):
        continue
    if row[0].isdigit():
        max = row[1].replace('*', '')
        min = row[2].replace('*', '')
        spread = abs(float(max)-float(min))
        if spread < normalday[1]:
            normalday = [row[0], spread]
print("Day: " + str(normalday[0]))
print("Smallest temperature spread: " + str(normalday[1]))


#Enoch Hang