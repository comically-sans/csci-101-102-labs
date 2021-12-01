# Dominic Pergola
# CSCI 102 - Section B
# Week 10 Lab
# Reference: zybooks csv section
# Time 90 minutes

import csv
dash_index = []
with open("formations.csv") as myfile:
    my_reader = csv.reader(myfile)
    file_list = []
    for row in my_reader:
        dash = row[0].find('-')
        dash_index.append(dash)
        file_list.append(row)

file_list[0].insert(1, 'Start Depth')
file_list[0].insert(2, 'End Depth')
file_list[0].insert(3, 'Difference in Depth')

i = 0
for l in file_list:
    if i >= 1:
        start_depth = round(float((l[0])[:dash_index[i]]), 2)
        end_depth = round(float((l[0])[dash_index[i] + 1:]), 2)
        diff_depth = round(float(end_depth) - float(start_depth), 2)
        if str(diff_depth)[-2] == '.':
            diff_depth = str(round(diff_depth, 2)) + '0'
        l.insert(1, start_depth)
        l.insert(2, end_depth)
        l.insert(3, diff_depth)
    i+=1

#print(file_list)
        
with open("formations_parsed.csv", 'w', newline = '') as newfile:
    writer = csv.writer(newfile)
    for line in file_list:
        writer.writerow(line)

'''with open("formations_parsed.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)'''
    
