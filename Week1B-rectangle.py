# Dominic Pergola
# CSCI 102 - Section H
# Week 1 - Part B
# Reference: Google for telling me that the max area for a rectangle with given perimeter is a square
# Time ~15 minutes

#ask for fence length
print("Please give total length of fencing available (in yds)")
length_yds = int(input("Length>"))

#convert to feet
length = length_yds * 3

#max area of a rectangle with a given perimeter will always be one with equal side lengths, e.g. a square

#find side lengths
side = float(length / 4)

#calculate area
area = round(side ** 2,1)

#print output
print("The maximum rectangular area that can be bound (in sqft) is:\nOUTPUT", area)
