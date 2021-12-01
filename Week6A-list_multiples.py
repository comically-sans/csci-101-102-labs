# Dominic Pergola
# CSCI 102 - Section H
# Week 6 - Part A
# Reference: zybooks for loops section
# Time ~15 minutes

#number input
print("Enter the number to create multiples for.")
num = int(input("NUMBER> "))

#index input
print("Enter the maximum index of the list.")
max_index = int(input("INDEX> "))

#iterate through range of index and append each value times the number to the list
multiple_list = []
for index in range(1, max_index + 2):

    multiple_list.append(num * index)

#print multiples list
print("Your list of multiples is as follows:")
print("OUTPUT", multiple_list)
